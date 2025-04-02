import json
import boto3
import csv
import io
from botocore.exceptions import ClientError

# AWS Services
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('your_table_name')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        # Extract S3 file details
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # Get the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')

        # Read CSV file
        csv_reader = csv.DictReader(io.StringIO(file_content))
        
        items_inserted = []
        for row in csv_reader:
            try:
                # Ensure required fields exist
                if 'id' not in row or 'timestamp' not in row or 'email' not in row or 'location' not in row or 'name' not in row:
                    print(f"Skipping row due to missing fields: {row}")
                    continue

                item = {
                    'id': row['id'].strip(),
                    'timestamp': row['timestamp'].strip(),
                    'email': row['email'].strip(),
                    'location': row['location'].strip(),
                    'name': row['name'].strip()
                }
                
                # Insert into DynamoDB only if unique
                try:
                    table.put_item(
                        Item=item,
                        ConditionExpression="attribute_not_exists(id) AND attribute_not_exists(timestamp)"
                    )
                    items_inserted.append(item)
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                        print(f"Skipping duplicate: {item}")
                    else:
                        raise e  # Re-throw error
                
            except Exception as e:
                print(f"Error processing row {row}: {str(e)}")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"File {file_key} processed", "inserted_items": items_inserted})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

# AWS Serverless Data Pipeline 🚀

## Overview
This project demonstrates a **serverless data pipeline** using **AWS Lambda, S3, and DynamoDB**. When a CSV file is uploaded to S3, Lambda processes it and stores structured data in DynamoDB.

## Architecture
![Architecture Diagram](https://tinyurl.com/mu7whec3)

## Technologies Used
- AWS S3 (Storage)
- AWS Lambda (Processing)
- AWS DynamoDB (Database)
- Python & Boto3 (AWS SDK)

## How It Works
1. Upload a CSV file to an **S3 bucket**.
2. An **S3 event** triggers the **Lambda function**.
3. Lambda reads and processes the file.
4. The structured data is stored in **DynamoDB**.

## Setup
1. Deploy the **Lambda function** (`lambda_function.py`).
2. Attach the correct **IAM policy** (`iam-policy.json`).
3. Configure an **S3 event trigger** for the Lambda function.
4. Test by uploading a CSV to S3!

## Author
👨‍💻 Yakkanti Revanth Reddy | Linkedin :https://tinyurl.com/mrbsus3m | GitHub : https://github.com/revanthreddy9/revanthreddy9
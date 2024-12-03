# AWS Lambda and API Gateway Project

## Overview
This project integrates AWS Lambda with API Gateway to create a serverless REST API. The Lambda function handles HTTP POST requests via API Gateway, processes data, and returns a response.

## Project Components
- **AWS Lambda**: Handles the backend logic, written in Python.
- **API Gateway**: Acts as the front door to accept HTTP requests and direct them to the Lambda function.

## Project Workflow
1. **Create a Lambda Function**:
   - Go to the **AWS Lambda Console** and create a new Lambda function.
   - Choose **Python** as the runtime and use the code in `lambda_function.py`.
   
2. **Create API Gateway**:
   - Open **AWS API Gateway** and create a **REST API**.
   - Create a **method (POST)** and link it to the Lambda function.
   - Enable **Lambda Proxy Integration** for seamless integration.
   - Deploy the API to a **new stage** (e.g., development).

3. **Testing the API**:
   - After deploying the API, copy the generated **endpoint URL**.
   - Use a browser or tools like **Postman** to send requests to the endpoint and verify the response.

## Requirements
- AWS Account with permissions to create Lambda functions and API Gateway.
- Basic knowledge of AWS Lambda, Python, and API Gateway.

## How It Works
- A **POST request** is made to the API Gateway.
- The API Gateway triggers the **Lambda function** to process the request.
- The Lambda function returns a response based on the method and event data.

## Benefits
- **Scalable and serverless** architecture.
- **Cost-effective** since Lambda charges are only for compute time used.
- **Secure** integration with proper access controls via API Gateway.

## Deployment Instructions
1. Log in to your **AWS Console**.
2. Create a new **Lambda function** with the provided Python code.
3. Create a new **REST API** in API Gateway, choose POST, and link to Lambda.
4. Deploy the API and **test** the endpoint URL.

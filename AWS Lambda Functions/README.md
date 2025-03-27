# Architecture

## AWS Lambda & API Gateway

This project involves deploying a serverless function on AWS Lambda, integrated with an API Gateway for handling HTTP requests.

### Components:
- **AWS Lambda**: Executes the backend function.
- **API Gateway**: Handles incoming HTTP requests and routes them to Lambda.
- **Python Function**: Defines the core logic.

## Lambda Function: `RandomDrinkFunction`

### Code Implementation
```python
def random_drink():
    drinks = ["coffee", "tea", "beer", "wine", "water", "juice"]
    return random.choice(drinks)

def lambda_handler(event, context):
    drink = random_drink()
    message = f"You should drink some {drink}"
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": message, "drink": drink})
    }
```

## Execution Results

### Status: Succeeded
#### Test Event: `Hello`
#### Response:
```json
{
    "statusCode": 200,
    "body": "{\"message\": \"You should drink some tea\", \"drink\": \"tea\"}"
}
```

## Deployment Steps
1. Upload the Python script to AWS Lambda.
2. Set up API Gateway to trigger the Lambda function.
3. Deploy and test the function via API Gateway.

## Notes
- Ensure necessary IAM permissions are set.
- API Gateway endpoint must be configured correctly.
- Debugging logs available in AWS CloudWatch.


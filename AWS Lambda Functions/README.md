# Architecture
<img width="1417" alt="Screenshot 2025-03-27 at 4 28 49 PM" src="https://github.com/user-attachments/assets/8044e3aa-9e1e-4294-af1e-ce991e758c66" />


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
<img width="1440" alt="Screenshot 2025-03-27 at 6 58 24 PM" src="https://github.com/user-attachments/assets/3548a0e6-8fb5-4433-bdba-1fe6fdb8f216" />

<img width="1439" alt="Screenshot 2025-03-27 at 7 18 21 PM" src="https://github.com/user-attachments/assets/2f2dd4da-761a-4a90-8b19-5717ff95e743" />





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
<img width="1440" alt="Screenshot 2025-03-27 at 6 57 40 PM" src="https://github.com/user-attachments/assets/edb63ff0-495d-4c32-86b0-c35a75cf9636" />

<img width="1440" alt="Screenshot 2025-03-27 at 6 59 26 PM" src="https://github.com/user-attachments/assets/a28461f9-47f8-4769-bf18-f551da466b6f" />




## Deployment Steps
1. Upload the Python script to AWS Lambda.
2. Set up API Gateway to trigger the Lambda function.
3. Deploy and test the function via API Gateway.

## For live demo
click this link https://6fnbdjmax1.execute-api.us-east-1.amazonaws.com/default/RandomDrinkFunction


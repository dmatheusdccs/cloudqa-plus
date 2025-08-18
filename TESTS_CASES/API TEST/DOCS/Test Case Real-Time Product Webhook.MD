Test Case: Real-Time Product Webhook Processing

	Objective

Validate that when a product is updated in the system, the configured webhook triggers correctly and processes the real-time data.


	Prerequisites


AWS account set up with:

API Gateway (HTTP API)

Lambda function (cloudqa-webhook-handler)

DynamoDB table (ProductUpdates)



Postman (or similar API testing tool) installed.

Project connected to GitHub repository.

Test environment prepared under C:\Users\Lenovo\Desktop\cloudqa-plus\TESTS_CASES\API TEST.


	Test Steps


Open Postman.

Create a POST request to the API Gateway Invoke URL:

https://.execute-api..amazonaws.com/default/webhook

copy
download
3. Go to the **Body** tab in Postman and select **raw → JSON**.
4. Enter the following test payload:
```json
{
  "productId": "AP001",
  "name": "Test Product",
  "price": 99.99,
  "status": "Updated"
}
Click Send to execute the request.
Observe the response from API Gateway. Expected:
HTTP Status Code: 200
Body:
copy
download
{
  "message": "Product update received"
}
Verify the DynamoDB table (ProductUpdates) to confirm the new item was inserted.

Check CloudWatch Logs for the Lambda function to ensure the webhook event was processed without errors.

	Expected Results

The webhook correctly triggers the Lambda function.
Lambda stores the incoming product update into DynamoDB.
DynamoDB table contains a new item with the provided productId.
CloudWatch Logs show successful execution with no errors.

	Post-Conditions

Test payload data is stored in DynamoDB for verification.
API Gateway, Lambda, and DynamoDB integration confirmed working as expected.

	Status

Pass if response = 200, item exists in DynamoDB, and logs confirm correct processing.
Fail otherwise.
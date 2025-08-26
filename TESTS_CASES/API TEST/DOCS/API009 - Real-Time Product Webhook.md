API009 - Real-Time Product Webhook Processing



Description



This test case validates the end-to-end real-time webhook processing flow when a product is updated in BigCommerce.



The objective is to ensure that product updates trigger a webhook event that is successfully received, processed by AWS Lambda, logged in CloudWatch, and stored in DynamoDB.







Preconditions





&nbsp;	1. BigCommerce API Access – Valid API credentials (API token and store hash) are available.



&nbsp;	2. DynamoDB Table – A table named WebhookEvents exists with:



Partition key: eventId (String)



Sort key: timestamp (Number, optional)



On-Demand capacity and encryption enabled.







&nbsp;	3.Lambda Function – Function cloudqa-webhook-handler is deployed and integrated with API Gateway (/cloudqa-webhook-transform).



&nbsp;	4. IAM Role and Permissions – IAM role cloudqa-webhook-handler-role with the following policies:



AWSLambdaBasicExecutionRole



AmazonDynamoDBFullAccess







&nbsp;	5.Test Environment Setup – Tools like Postman or pytest are available with environment variables for:



API endpoint



Authentication token



Region







&nbsp;	6. Test Product Available – A product exists in BigCommerce (e.g., product ID 103) to trigger updates.







Test Steps





**1. Send PUT Request to Update Product:**



http



PUT /v3/catalog/products/103

Content-Type: application/json

X-Auth-Token: <your\_token>



{

&nbsp; "price": "7.99"

}





Expected: Response 200 OK with updated product details.





**2. Verify CloudWatch Logs:**



Navigate to AWS Console → CloudWatch → Log Groups → /aws/lambda/cloudqa-webhook-handler.

Expected log entry:

ini



Event received: productId=103

EventType=store/product/updated

StoreHash=<valid\_store\_hash>

Price=7.99





**3. Verify DynamoDB Record:**



&nbsp;	Go to DynamoDB Console → Table WebhookEvents → Explore Items.

&nbsp;	Expected new record:

&nbsp;		eventId: unique identifier (evt103\_timestamp)

&nbsp;		timestamp: UTC timestamp

&nbsp;		eventType: store/product/updated

&nbsp;		productId: 103

&nbsp;		price: 7.99

&nbsp;		storeHash: correct store hash





**4. Validation Summary:**



Postman/pytest returns 200 OK.

CloudWatch logs show event payload for product 103.

DynamoDB contains new record with correct values.





**Expected Results:**



Product is successfully updated in BigCommerce.

API Gateway receives the webhook event.

Lambda function processes and logs the event.

DynamoDB stores a new record with correct event details.

CloudWatch provides traceable logs for the invocation.





**Error Handling:**



If parsing or DynamoDB insertion fails, Lambda should return HTTP 500 with a clear error message.

All failures should still be visible in CloudWatch Logs.





Evidence Checklist

&nbsp;Postman response screenshot with 200 OK.

&nbsp;CloudWatch log entry screenshot.

&nbsp;DynamoDB record screenshot showing new item.




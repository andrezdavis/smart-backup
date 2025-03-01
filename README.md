# Smart Backup Lightweight Service
Data loss can be a major headache for businesses, leading to lost revenue, compliance issues, and unhappy customers. This project ensures that every payment transaction is automatically backed up in Amazon S3 while being written to the main database without any manual effort.

A smart backup system like this helps businesses:

1. Prevent data loss from crashes
2. Improve System Latency with asynchronous backup processing
3. Keep writes loosely coupled
4. Maintain customer trust by ensuring payment records are always accurate
5. Save time and effort by automating backups
## Application Flow
Application Sends a Payment Write Event
- The payment application writes a processed payment to some MySQL/PostgreSQL DB then sends an event to AWS EventBridge via the <code>put_events()</code> API call.

EventBridge receives the event and checks rules to determine if the event matches any conditions.
```
{
  "source": "payment.service",
  "detail-type": "PaymentProcessed",
  "detail": {
    "transaction_id": "12345",
    "amount": 100,
    "currency": "USD",
    "status": "Completed"
  }
}
```
The event is routed to an AWS Lambda function once the lambda is triggered.

Lambda receives the event and extracts payment data from the detail field.
It saves the extracted payment data to an Amazon S3 backup storage.
The backup is available in S3 for retrieval in case of failures.

Pictures shown below to illustrate AWS flow.


![postResponse](https://github.com/user-attachments/assets/22bfea49-9198-4480-9c03-ef51a9a29bf4)

-----

![EventBridgepic](https://github.com/user-attachments/assets/46fc2f7e-2539-49fe-a328-318b75c3aeca)

-----

![InvokeLambda](https://github.com/user-attachments/assets/5036944b-d6e5-407f-9310-68612cd9c3c0)

-----

![LambdaMetrics](https://github.com/user-attachments/assets/be3fa613-d70b-4199-bba4-7e30fa4448bd)

-----

![eventbucket](https://github.com/user-attachments/assets/6034ca9c-4994-4c9e-bbb7-a8dd96d7b754)

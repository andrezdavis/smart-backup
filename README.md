# Smart Backup Lightweight Service
Data loss can be a major headache for businesses, leading to lost revenue, compliance issues, and unhappy customers. This project ensures that every payment transaction is automatically backed up in Amazon S3 while being written to the main database without any manual effort.

A smart backup system like this helps businesses:

1. Prevent data loss from crashes or cyberattacks
2. Stay compliant with financial regulations
3. Maintain customer trust by ensuring payment records are always accurate
4. Save time and effort by automating backups
5. By using EventBridge, Lambda, and S3, businesses get a reliable, hands-off backup system that keeps critical payment data safe and accessible.
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

Lambda receives the event and extracts payment data from the detail field. It saves the extracted payment data to an Amazon S3 backup storage.
The backup is available in S3 for retrieval in case of failures.

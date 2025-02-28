from flask import Flask, request, jsonify
import json
import boto3
import uuid
import datetime
import os

app = Flask(__name__)

eventbridge_client = boto3.client('events', region_name="us-east-2")

EVENT_BUS_NAME = "default"
EVENT_SOURCE = "payment.app"

@app.route('/process-payment', methods=['POST'])
def process_payment():
    try:
        data = request.json

        payment_event = {
            "payment_id": str(uuid.uuid4()),
            "amount": data.get("amount"),
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "user_id": data.get("user_id"),
            "status": "processed"
        }
        response = eventbridge_client.put_events(
            Entries=[
                {
                    'Source': EVENT_SOURCE,
                    'DetailType': 'PaymentProcessed',
                    'Detail': json.dumps(payment_event),
                    'EventBusName': EVENT_BUS_NAME
                }
            ]
        )
        return jsonify({"message": "Payment event sent", "event_id": response['Entries'][0]['EventId']}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

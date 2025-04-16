# tasks/notifications.py
import boto3
from celery import shared_task

sns_client = boto3.client('sns', region_name=AWS_REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@shared_task
def send_sns_notification(phone_number, message):
    response = sns_client.publish(
        PhoneNumber=phone_number,
        Message=message
    )
    return response
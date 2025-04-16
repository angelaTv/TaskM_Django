import boto3
from django.conf import settings

sns_client = boto3.client(
    'sns',
    region_name=settings.AWS_REGION_NAME,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)

def send_sns_notification(phone_number, message):
    response = sns_client.publish(
        PhoneNumber=phone_number,
        Message=message
    )
    return response

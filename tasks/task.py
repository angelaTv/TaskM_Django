from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_reminder(task_id, user_email):
    send_mail(
        subject="Task Reminder",
        message=f"Reminder for task {task_id}",
        from_email="noreply@example.com",
        recipient_list=[user_email]
    )
    return f"Reminder sent for task {task_id}"

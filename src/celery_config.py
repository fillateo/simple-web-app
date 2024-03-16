from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["src.tasks"],
)

celery_app.conf.beat_schedule = {
    "send-scheduled-emails-task": {
        "task": "src.tasks.send_scheduled_emails",
        "schedule": crontab(minute="*/1"),
    },
}

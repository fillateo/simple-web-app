import datetime

from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.event import Event
from tests.resources import AppTestBase


class Test(AppTestBase):

    def setUp(self) -> None:
        super(Test, self).setUp()
        self.setup_database()
        self.email_service = self.app.container.email_service()

    def create_sample_event(self):
        event = Event(name="Sample Event")
        db.session.add(event)
        db.session.commit()

    def test_create(self):
        self.create_sample_event()
        data = {
            "event_id": 1,
            "email_subject": "Example subject 3",
            "email_content": "Example email content",
            "timestamp": "15 Dec 2015 23:12",
        }
        email = self.email_service.create(data)
        self.assertEqual(email.event_id, 1)
        self.assertEqual(email.email_subject, "Example subject 3")
        self.assertEqual(email.email_content, "Example email content")
        self.assertEqual(email.timestamp, datetime.datetime(2015, 12, 15, 23, 12))

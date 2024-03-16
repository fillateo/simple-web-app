import json

from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.event import Event
from tests.resources import AppTestBase


class Test(AppTestBase):

    def setUp(self) -> None:
        super(Test, self).setUp()
        self.setup_database()

    def create_sample_event(self):
        event = Event(name="Sample Event")
        db.session.add(event)
        db.session.commit()

    def test_send_email(self):
        self.create_sample_event()
        data = {
            "event_id": 1,
            "email_subject": "Example subject 3",
            "email_content": "Example email content",
            "timestamp": "15 Dec 2015 23:12",
        }
        response = self.client.post(
            "email", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.data)
        self.assertEqual(data, response_data)

    def test_send_email_unicode_compliant(self):
        self.create_sample_event()
        data = {
            "event_id": 1,
            "email_subject": "Example subject with Unicode 🚀",
            "email_content": "Example email content with Unicode ✓",
            "timestamp": "15 Dec 2015 23:12",
        }
        response = self.client.post(
            "email", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.data)
        self.assertEqual(data, response_data)

    def test_send_email_event_not_found(self):
        self.create_sample_event()
        data = {
            "event_id": 2,
            "email_subject": "Example subject 3",
            "email_content": "Example email content",
            "timestamp": "15 Dec 2015 23:12",
        }
        response = self.client.post(
            "email", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(400, response.status_code)
        response_data = json.loads(response.data)
        self.assertEqual({"error_message": "Event with id 2 not found"}, response_data)

    def test_send_email_empty_data(self):
        self.create_sample_event()
        response = self.client.post(
            "email", data=json.dumps({}), content_type="application/json"
        )
        self.assertEqual(400, response.status_code)
        response_data = json.loads(response.data)
        self.assertEqual({"error_message": "No data provided"}, response_data)

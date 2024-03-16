from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension


class Email(db.Model, ModelExtension):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(
        db.Integer, db.ForeignKey("events.id"), nullable=False
    )  # Define foreign key relationship
    email_subject = db.Column(db.String(100), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean, default=False)

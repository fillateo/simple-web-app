from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension

event_user_association_table = Table(
    "event_user_association",
    db.metadata,
    Column("event_id", Integer, ForeignKey("events.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
)


class Event(db.Model, ModelExtension):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    users = relationship(
        "User", secondary=event_user_association_table, back_populates="events"
    )

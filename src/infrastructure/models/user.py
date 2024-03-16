from sqlalchemy.orm import relationship

from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension

from .event import event_user_association_table


class User(db.Model, ModelExtension):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    events = relationship(
        "Event", secondary=event_user_association_table, back_populates="users"
    )

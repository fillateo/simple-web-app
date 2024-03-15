from datetime import datetime

from marshmallow import Schema, fields


class CustomTimestampField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.strftime("%d %b %Y %H:%M")

    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        try:
            return datetime.strptime(value, "%d %b %Y %H:%M")
        except ValueError as e:
            raise fields.ValidationError(str(e))


class EmailSchema(Schema):
    event_id = fields.Integer(required=True)
    email_subject = fields.String(required=True)
    email_content = fields.String(required=True)
    timestamp = CustomTimestampField(required=True)

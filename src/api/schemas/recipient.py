from marshmallow import Schema, fields


class RecipientSchema(Schema):
    id = fields.Integer(required=True)
    email_address = fields.Email(required=True)

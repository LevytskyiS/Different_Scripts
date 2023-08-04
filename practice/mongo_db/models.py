from datetime import datetime

from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, StringField, IntField


class ProductData(Document):
    title = StringField()
    productId = StringField()
    link = StringField()
    status = StringField()
    created_at = DateTimeField()
    is_informed = BooleanField()


class User(Document):
    user_id = IntField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    created = DateTimeField(default=datetime.now())
    is_active = BooleanField(default=True)

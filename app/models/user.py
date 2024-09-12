from mongoengine import Document, EmailField, StringField, IntField


class User(Document):
    username: str = StringField()
    email: str = EmailField()
    age: int = IntField()

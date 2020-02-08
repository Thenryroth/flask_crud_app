from flask import Flask
from models import db

class Book(db.Model):
    id = db.Column(
        db.Integer(),
        unique=True,
        nullable=False,
        primary_key=True
    )
    author = db.Column(
        db.String(80),
        nullable=False
    )
    title = db.Column(
        db.String(80),
        nullable=False
    )

    def __repr__(self):
        return "<Title: {}>".format(self.title)

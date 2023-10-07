"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://tcvets.com/wp-content/uploads/sites/164/2022/06/tcvets-placeholder-1.png'


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet"""

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(30),
        nullable=False
        )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE
    )

    age = db.Column(
        db.Text,
        nullable=False
    )
    # might need to change to options

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

from . import db

class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    type = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    duration = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    dicription = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    prise = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    tags = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    slug = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    filename = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    
    def __repr__(self):
        return '<Song {}>'.format(self.name)
from . import db
from geoalchemy2 import Geometry

class post(db.Model):
    latlon=db.Column(Geometry('POINT'))

    created = db.Column(
        db.DateTime,
        primary_key=True
    )
    post=db.Column(
        db.String()
    )
    lat=db.Column(
        db.String()
    )
    lon=db.Column(
        db.String()
    )

    def __repr__(self):
        return '<POST {self.post}>'
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates
from datetime import datetime, timezone

from app import db

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    uploader = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)

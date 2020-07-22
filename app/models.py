from datetime import datetime
from app import db

class Schools(db.Model):
    __tablename__ = 'test'
    __table_args__ = { 'extend_existing': True }
    Name = db.Column(db.Text, primary_key=True)  

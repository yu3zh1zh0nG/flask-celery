from flask_sqlalchemy import SQLAlchemy

from app import db

class Article(db.Model):
    __tablename__ = 'article'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)



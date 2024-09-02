#!/usr/bin/env python3

"""
Blogs table
"""
from models.base_model import BaseModel, db


class Blog(BaseModel, db.Model):
    """
    Blog's Table
    Args:
        name: name of the blog
        description: description of the blog
        blog_content: Content of the blog
    """
    __tablename__ = 'blogs'
    user_id = \
        db.Column(db.String(126), db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(126), nullable=False)
    desription = db.Column(db.String(126), nullable=False)
    blog_content = db.Column(db.Text, nullable=False)

from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import current_user, login_required
from models.users import User
from models.blogs import Blog
from routes import api
from config import db, app


@api.route('/blogs', methods=['GET'], strict_slashes=False)
#@login_required
def blog():
    return jsonify({"message": "Blog with me"})
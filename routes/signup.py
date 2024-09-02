from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import current_user
from models.users import User
from routes import api
from flask_mail import Message
from random import randint
from config import mail  

def generate_verification_code():
    """
    Generate a random 6-digit verification code
    """
    return randint(100000, 999999)

@api.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    """
    Register a new user
    """
    if current_user.is_authenticated:
        return jsonify({'message': 'User already logged in'}), 400
    
    form = request.get_json()
    if not form:
        return jsonify({"error": "Not a JSON"})
    
    # Check for required fields
    required_fields = ["username", "email", "password", "first_name", "last_name"]
    for field in required_fields:
        if field not in form:
            return jsonify({"error": f"Missing {field}"})
    username = form.get("username")
    email = form.get("email")
    password = form.get("password")
    first_name = form.get("first_name")
    last_name = form.get("last_name")
    verification_code = generate_verification_code()
    if User.find_obj_by(username=username):
        return jsonify({'message': 'Username already exists'}), 400
    if User.find_obj_by(email=email):
        return jsonify({'message': 'Email already exists'}), 400
    user = User(
        **{
            'username': username,
            'email': email,
            'password': User.hash_password(password),
            'first_name': first_name,
            'last_name': last_name,
            'verification_code': verification_code
        }
    )
    user.save()
    #send verification code
    msg = Message("Verification Code", recipients=[email])
    msg.body = f"Your verification code is {verification_code}"
    mail.send(msg)
    return jsonify({
        'message': 'User created successfully, check your email for verification code',
        'status': 201
        }), 201

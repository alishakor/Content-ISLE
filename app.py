from flask import jsonify, Response, render_template, session
from models.base_model import app
from models.users import User
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_cors import CORS
from routes import api
import logging
from flask_mail import Mail, Message
from config import mail
# from flask_wtf.csrf import CSRFProtect, generate_csrf

app.register_blueprint(api)
# csrf = CSRFProtect(app)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


@app.errorhandler(404)
def error(error) -> Response:
    return jsonify({"error": "Not found"})


@app.errorhandler(403)
def forbidden_err(error):
    return jsonify({"error": "Unauthorized"})


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Islamic Resource Center"})

@app.route('/send_email')
def send_email():
    try:
        msg = Message("Hello from Flask", recipients=["aliushakor13@gmail.com"])
        msg.body = "This is a test email sent from a Flask application!"
        mail.send(msg)
        return "Email sent!", 200
    except Exception as e:
        app.logger.error(f"Failed to send email: {e}")
        print((f"Failed to send email: {e}"))
        return "Failed to send email", 500




# @app.route('/token', methods=['GET'])
# def token():
#     csrf_token = generate_csrf()
#     session['csrf_token'] = csrf_token
#     session.modified = True
#     return jsonify({'X-CSRFToken': csrf_token})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#!/usr/bin/env python3
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/')

from routes.signup import *
from routes.blogs import *

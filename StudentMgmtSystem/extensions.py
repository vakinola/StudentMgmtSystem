from flask_sqlalchemy import SQLAlchemy
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    Flask,
    flash,
)
from flask_login import LoginManager
from flask_admin import Admin
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from urllib.parse import urlparse, urljoin

from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message


db = SQLAlchemy()
csrf = CSRFProtect()

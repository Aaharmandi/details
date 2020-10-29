from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")
    dropzone = Dropzone(app)
    
    app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

    app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
    app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
    # app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

    # Uploads settings
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
    db.init_app(app)
    with app.app_context():
        from . import routes
        db.create_all()
    return app
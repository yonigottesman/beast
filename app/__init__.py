from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_uploads import UploadSet, IMAGES, configure_uploads


images = UploadSet('images', IMAGES)
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
configure_uploads(app, (images,))

from app import routes

from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os
import re

app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)

# Load configuration
if 'WEBSITE_HOSTNAME' not in os.environ:
    app.config.from_object('azureproject.development')
else:
    app.config.from_object('azureproject.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# The import must be done after db initialization due to circular import issue
from models import Image

@app.route('/')
def index():
    # Redirect to the gallery page or render a placeholder page
    return render_template('index.html', restaurants=[])

@app.route('/upload-log', methods=['GET'])
def upload_log():
    # Query all images to simulate an upload log
    logs = Image.query.order_by(Image.upload_date.desc()).all()
    return render_template('upload_log.html', logs=logs)

@app.route('/add', methods=['POST'])
@csrf.exempt
def upload_image():
    try:
        uploader = request.form.get('uploader')
        image = request.files.get('image')

        if not uploader or not re.match(r'^[a-zA-Z0-9]+$', uploader):
            return "Invalid uploader username. It must be alphanumeric.", 400

        if not image:
            return "No image file provided.", 400

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.static_folder, 'uploads', filename)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        image.save(image_path)

        image_url = url_for('static', filename=f'uploads/{filename}')
        new_image = Image(uploader=uploader, image_url=image_url)
        db.session.add(new_image)
        db.session.commit()

        return f"Image uploaded successfully by {uploader}.", 201
    except Exception as e:
        return f"Error uploading image: {str(e)}", 500

@app.route('/gallery', methods=['GET'])
def gallery():
    try:
        images = Image.query.all()
        return render_template('gallery.html', images=images)
    except Exception as e:
        # En producción podrías querer loggear el error en lugar de mostrarlo
        return f"Error accessing gallery: {str(e)}", 500
    
# Prueba
@app.route('/test', methods=['GET'])
def test():
    print("Test endpoint hit")
    return "Test endpoint is working!"
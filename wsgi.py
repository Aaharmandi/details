from application import create_app
import os
app = create_app()
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config.update(
#     UPLOADED_PATH=os.path.join(basedir, 'uploads'),
#     # Flask-Dropzone config:
#     DROPZONE_ALLOWED_FILE_TYPE='image',
#     DROPZONE_MAX_FILE_SIZE=3,
#     DROPZONE_MAX_FILES=30,
# )
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
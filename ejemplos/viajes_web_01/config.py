class Config():
    SECRET_KEY = 'cepy2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///viajes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER='static/uploads'
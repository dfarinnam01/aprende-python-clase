class Config:
    SECRET_KEY = 'tu-clave-secreta-aqui-cambiala-por-una-segura'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///viajes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de uploads
    UPLOAD_FOLDER = 'uploads'
    UPLOAD_FOLDER_IMAGES = f'{UPLOAD_FOLDER}/images'
    UPLOAD_FOLDER_IMAGES_THUMBNAILS = f'{UPLOAD_FOLDER_IMAGES}/thumbnails'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB máximo
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

    # Tamaño de las imágenes
    IMAGE_SIZE = (800, 600)
    THUMBNAIL_SIZE = (300, 200)
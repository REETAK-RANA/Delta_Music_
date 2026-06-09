import os

class Config:
    SECRET_KEY = "delta_music_super_secret_key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///delta_music.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_MUSIC = os.path.join(
        "static",
        "music"
    )

    UPLOAD_IMAGES = os.path.join(
        "static",
        "images"
    )
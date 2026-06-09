from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )


class Song(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200)
    )

    artist = db.Column(
        db.String(200)
    )

    genre = db.Column(
        db.String(100)
    )

    music_file = db.Column(
        db.String(255)
    )

    cover_image = db.Column(
        db.String(255)
    )


class Favorite(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    song_name = db.Column(
        db.String(200)
    )


class RecentPlay(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    song_name = db.Column(
        db.String(200)
    )


class Playlist(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    playlist_name = db.Column(
        db.String(200)
    )


class PlaylistSong(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    playlist_id = db.Column(
        db.Integer
    )

    song_name = db.Column(
        db.String(200)
    )
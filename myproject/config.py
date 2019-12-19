import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'benim-gizli-anahtarim'

    # DATABASE
    my_path = 'sqlite:///' + os.path.join(BASEDIR, 'veritabani.db')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or my_path

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Uploading configuration
    UPLOADED_PHOTOS_DEST = os.path.join(BASEDIR, 'myapp/static/img')

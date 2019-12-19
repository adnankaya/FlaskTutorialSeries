# external
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# internal
from myapp import db, login


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(60))
    password = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(120))
    about_me = db.Column(db.String(280))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    author = db.Column(db.String(60), nullable=False)
    publish_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

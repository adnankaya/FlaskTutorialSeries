from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    password = PasswordField('Parola', validators=[DataRequired()])
    remember_me = BooleanField('Beni Hatırla!')
    submit = SubmitField('Giriş Yap')


class RegisterForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parola', validators=[DataRequired()])
    submit = SubmitField('Kaydol')


class AboutForm(FlaskForm):
    about_me = StringField('Hakkımda', validators=[DataRequired()])
    submit = SubmitField('Kaydet')


class BookForm(FlaskForm):
    title = StringField('', validators=[DataRequired()])
    author = StringField('', validators=[DataRequired()])
    year = StringField('', validators=[DataRequired()])
    month = StringField('', validators=[DataRequired()])
    day = StringField('', validators=[DataRequired()])


class CheckBoxForm(FlaskForm):
    pass
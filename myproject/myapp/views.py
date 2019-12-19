from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
import datetime

from myapp import app, db, photos
from myapp.forms import LoginForm, RegisterForm, AboutForm, BookForm, CheckBoxForm
from myapp.models import User, Book


@app.route('/', methods=['GET', 'POST'])
@app.route('/anasayfa', methods=['GET', 'POST'])
@login_required
def index():
    form = CheckBoxForm()
    books = Book.query.filter_by(user_id=None).all()
    if form.validate_on_submit():
        selected_books = request.form.getlist('selected_books')
        for id in selected_books:
            book = Book.query.get(id)
            book.user_id = current_user.id
            db.session.add(book)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('index.html', title='Anasayfa', form=form, books=books)


@app.route('/users')
@app.route('/users/<id>')
@login_required
def users(id=None):
    users = User.query.all()
    if id is not None:
        user = User.query.get(id)
        title = user.username+"'in Profili"
        books = Book.query.filter_by(user_id=id).all()
        return render_template('profile.html', title=title, user=user, books=books)
    return render_template('users.html', title='Kullanıcılar Listesi', users=users)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', title="Profil", user=current_user, books=books)


@app.route('/give_back/<book_id>')
@login_required
def give_back(book_id):
    book = Book.query.get(book_id)
    book.user_id = None
    db.session.commit()
    return redirect(url_for('profile'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Kullanıcı adı veya parola hatalı!", "danger")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Giriş Yap', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title="Kaydol", form=form)


@app.route('/edit_about_me', methods=['GET', 'POST'])
@login_required
def edit_about_me():
    form = AboutForm()
    if form.validate_on_submit():
        about_me = form.about_me.data
        current_user.about_me = about_me
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('about_form.html', title='Hakkımda Ekle', form=form)


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        current_user.photo_url = filename
        db.session.commit()
        return redirect(url_for('profile'))


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    books = Book.query.all()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        year = int(form.year.data)
        month = int(form.month.data)
        day = int(form.day.data)
        date_time = datetime.date(year, month, day)

        book = Book(title=title, author=author, publish_date=date_time)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('add_book'))

    return render_template('book.html', title="Kitap Ekle", form=form, books=books)

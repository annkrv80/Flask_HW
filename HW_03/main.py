#Создать форму для регистрации пользователей на сайте. 
#Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
#При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from models import db, User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/')
def index():
    return redirect(url_for('register'))


pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username =form.username.data
        surname = form.surname.data
        email = form.email.data
        psw = form.password.data
        if re.match(pattern, psw):
            password = generate_password_hash(psw)
        else:
            return f'Пароль должен содержать буквы в верхнем и нижнем регистре, хотя бы одну цифру и 8 символов'
        existing_user = User.query.filter(User.email == email).first()
        if existing_user:
            error_msg = 'Пользователь с таким email уже существует.'
            form.username.errors.append(error_msg)
            return render_template('register.html', form=form)
        new_user = User(username=username, surname=surname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

       
        success_msg = 'Регистрация прошла успешно!'
        return success_msg

    return render_template('register.html', form=form)



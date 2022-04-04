# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class RegisterForm(FlaskForm):
    email = EmailField('Login / email', validators=[
        DataRequired('Вы не ввели логин/почту')
    ])

    password = PasswordField('Password', validators=[
        DataRequired('Вы не ввели пароль'),
    ])

    password2 = PasswordField('Repeat password', validators=[
        DataRequired('Вы не повторили пароль'),
    ])

    surname = StringField('Surname', validators=[
        DataRequired('Вы не ввели фамилию'),
    ])

    name = StringField('Name', validators=[
        DataRequired('Вы не ввели имя'),
    ])

    age = IntegerField('Age', validators=[
        DataRequired('Вы не ввели возраст'),
        NumberRange(min=1, message='Нельзя регистрироваться, если вам меньше 1 года')
    ])

    position = StringField('Position', validators=[
        DataRequired('Вы не ввели должность')
    ])

    speciality = StringField('Speciality', validators=[
        DataRequired('Вы не ввели профессию')
    ])

    address = StringField('Address', validators=[
        DataRequired('Вы не ввели адрес')
    ])

    submit = SubmitField('Submit')

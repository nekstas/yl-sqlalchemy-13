# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from flask import Flask, render_template
from flask_restful import Api

from api import jobs_api, users_resource
from data import db_session
from data.db_session import create_session
from data.users import User
from forms.register_form import RegisterForm

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'mars_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    message = ''
    if form.validate_on_submit():
        with create_session() as session:
            if form.password.data != form.password2.data:
                message = 'Пароли не совпадают'
            elif session.query(User).filter(User.email == form.email.data).all():
                message = 'Пользователь с такой почтой уже существует'
            else:
                user = User()

                user.email = form.email.data
                user.surname = form.surname.data
                user.name = form.name.data
                user.age = form.age.data
                user.position = form.position.data
                user.speciality = form.speciality.data
                user.address = form.address.data
                user.set_password(form.password.data)

                session.add(user)
                session.commit()

                message = 'Вы успешно зарегистрировались'

    return render_template('register.html', form=form, message=message)


def main():
    db_session.global_init('db/mars.db')

    # api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

    app.register_blueprint(jobs_api.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()


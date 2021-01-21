from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Suriya'}
    posts = [{
        'author': {'username': 'Suriya'},
        'body': 'I am going to Master movie today'
    }, {
        'author': {'username': 'Srinidhi'},
        'body': 'All credits to me'
    }]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request received for user {form.username.data} and remember_me {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

from flask import render_template
from app import app

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

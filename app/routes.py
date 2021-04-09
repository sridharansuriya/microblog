from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Suriya'}
    posts = [
        {
            'author': {'username': 'Suriya'},
            'body': 'Hot day in Chennai'
        },
        {
            'author': {'username': 'Srinidhi'},
            'body': 'CWC FTW!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

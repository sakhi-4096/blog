from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sakhile'}
    posts = [
        {
		'author': {'username': 'Zethembiso'},
		'body': 'Kade sidla isigwamba namuhla!'
	},
       {
	       'author': {'username': 'Bongeka'},
	       'body': 'Ngike ngaya edolobheni namuhla kugcwele yazi'
	}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

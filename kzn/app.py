import os
import json

from flask import Flask, session, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
	if 'username' in session:
		return """
<form action = "/logout", method = "post">
  <button type="submit" class="btn btn-default">Logout</button>
</form>"""
	else:
		return render_template('home.html')

@app.route("/login", methods=['POST'])
def login():
	session['username'] = request.form['email']
	return redirect(url_for('home'))

@app.route("/logout", methods=['POST'])
def logout():
	session.pop('username', None)
	return redirect(url_for('home'))

@app.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "GET":
        return render_template('board.html')
    elif request.method == "POST":
        return redirect(url_for('board'))

@app.route("/read", methods=["GET"])
def read():
	arts = []
	for file in os.listdir('data/'):
		with open('data/' + file) as f:
			arts.append(json.load(f))
	return render_template('read.html', articles=arts)

@app.route("/write", methods=["GET", "POST"])
def write():
	if request.method == 'GET':
		return render_template('write.html')
	elif request.method == 'POST':
		dic = dicfy(request.form['title'], request.form['text'], now())
		with open('data/' + hash(), 'w') as f:
			json.dump(dic, f)
		return redirect(url_for('read'))

from random import randrange
def hash(len=10):
	return ''.join([ str(randrange(0, 9)) for _ in range(len) ])

def dicfy(title, text, date):
	d = {
		'title': title,
		'text': text,
		'date': date,
	}
	return d

def now():
	return datetime.now().strftime('%Y-%m-%d')

if __name__ == "__main__":
	app.secret_key = 'asdfaxcbaxba'
	app.run(host='0.0.0.0', debug=True)

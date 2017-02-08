from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    if 'username' in session:
        return """
<div class="col-md-6 col-md-offset-3">
  <form action="/logout" method="POST">
    <button type="submit" class="btn btn-default">Logout</button>
  </form>
</div>
        """
    else:
        return render_template('home.html')

@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['email']
    return redirect('/')

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect('/')

import os
import json
@app.route("/read", methods=["GET"])
def read():
    arts = []
    for file in os.listdir('data/'):
        with open('data/' + file, 'r') as f:
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

from datetime import datetime
def now():
    return datetime.now().strftime('%Y-%m-%d')

# main
if __name__ == "__main__":
    app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', debug=True)

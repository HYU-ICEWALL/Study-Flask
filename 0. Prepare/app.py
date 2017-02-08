from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    if 'username' in session:
        return """
<form action="/logout" method="POST">
  <button type="submit" class="btn btn-default">logout</button>
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

# main
if __name__ == "__main__":
    app.secret_key = 'a'
    app.run(host='0.0.0.0', debug=True)






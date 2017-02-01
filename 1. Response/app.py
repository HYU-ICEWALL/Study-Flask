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

# main
if __name__ == "__main__":
    app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', debug=True)

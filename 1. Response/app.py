from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/login", methods=['POST'])
def login():
    print (request.form)
    return redirect('/')


# main
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

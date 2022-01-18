from flask import *

app = Flask(__name__)


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route('/')
def site():
    return render_template("site.html")


@app.route("/gloves")
def gloves():
    return render_template("latex_gloves.html")


if __name__ == '__main__':
    app.run(debug=True)
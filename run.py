from flask import Flask, url_for, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    """

    :return: 
    """
    return render_template('home.html')


@app.route('/about/')
def about():
    """

    :return:
    """
    return render_template('about.html')


@app.route('/contact/')
def contact():

    """

    :return:
    """
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
debug = 'True'

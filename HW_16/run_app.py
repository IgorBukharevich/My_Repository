"""
Applications for storing links to my repository
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    function for calling templates from the 'templates' folder
    :return: template 'index.html '
    """
    return render_template('index.html')


@app.route('/my_repository')
def my_repository():
    """
    function for calling a link to my repository
    :return: My Repository link
    """
    return '<a href="https://github.com/IgorBukharevich/My_Repository">My Repository</a>'


@app.route('/pull')
def my_pull():
    """
    function for calling a link to my pull requests
    :return: My pull request link
    """
    return '<a href="https://github.com/IgorBukharevich/My_Repository">My pull requests</a>'


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

"""APP flask Registration
"""
from werkzeug.security import generate_password_hash
from flask import Flask
from flask import render_template
from flask import request
from settings import *
from models import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# postgres connections
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f'{DIALECT_DB}://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Add Register Users"""
    if request.method == 'POST':

        try:
            hash_a = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash_a)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], age=request.form['age'],
                         city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print('Error Add DataBase')
    return render_template('registration.html')


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(HOST, PORT, DEBUG)

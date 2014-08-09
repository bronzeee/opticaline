__author__ = 'xu'
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bronze@121.40.88.181/opticaline'


@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(405)
def not_found(error):
    return render_template('error/404.html'), 405


@app.errorhandler(500)
def not_found(error):
    return render_template('error/500.html'), 500


from web import action
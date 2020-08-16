from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_pyfile("settings.py")

import views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

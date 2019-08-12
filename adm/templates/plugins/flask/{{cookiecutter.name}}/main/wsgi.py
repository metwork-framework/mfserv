import os
import mflog
from flask import Flask, render_template


app = Flask(__name__)
if os.environ.get('MFSERV_CURRENT_PLUGIN_DEBUG', '0') == '1':
    app.config['PROPAGATE_EXCEPTIONS'] = True
logger = mflog.get_logger(__name__)


@app.route("/{{cookiecutter.name}}/")
def hello_world():
    logger.info("This is an info message")
    return "Hello World !"


@app.route("/{{cookiecutter.name}}/<name>")
def hello(name="unknown"):
    return render_template("template_urlparse/index.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

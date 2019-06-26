"""
Main code of the template exemple to use Flask.
"""

from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

# Simple use of appi with jinja implements {%raw%}{{}}{%endraw%}
@app.route("/{{cookiecutter.name}}/")
def hello_world():
    return "Hello World !"
@app.route("/{{cookiecutter.name}}/<name>")
def hello(name="unknown"):
    return render_template("template_urlparse/index.html", name=name)

# rendering html (and other files types) template.
@app.route("/{{cookiecutter.name}}/webpage")
def webpage():
    return render_template("template_webpage/index.html")

template = Template('{% raw %}{{ name }}{% endraw %} je te salue')

# Insert variables with name and send it to the rendering.
@app.route("/{{cookiecutter.name}}/jinja2/<name>")
def jinja(name):
    return (template.render(name=name) +
            render_template("template_jinja_examples/index.html", name=name))

# Simple error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

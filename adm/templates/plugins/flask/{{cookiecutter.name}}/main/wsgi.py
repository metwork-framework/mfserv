"""
Flask template.
"""

from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

# Simple use of app with jinja implements ({%raw%}{{}}{%endraw%})
@app.route("/{{cookiecutter.name}}/")
def hello_world():
    return "Hello World !"

@app.route("/{{cookiecutter.name}}/<name>")
def hello(name="unknown"):
    return render_template("template_urlparse/index.html", name=name)

template = Template('Rendering template with variable:'
                    ' {% raw %}{{ name }}{% endraw %}')

# Insert variables with <> and send it to the rendering.
@app.route("/{{cookiecutter.name}}/jinja2/<name>")
def jinja(name):
    return (template.render(name=name) +
            render_template("template_jinja_examples/index.html", name=name))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)


template = Template('{% raw %}{{ name }}{% endraw %} je te salue')


@app.route("/{{cookiecutter.name}}/")
@app.route("/{{cookiecutter.name}}/<name>")
def hello(name="unknown"):
    return render_template("template_urlparse/index.html", name=name)


@app.route("/{{cookiecutter.name}}/webpage")
def webpage():
    return render_template("template_webpage/index.html")


@app.route("/{{cookiecutter.name}}/jinja2/<name>")
def jinja(name):
    return (template.render(name=name) +
            render_template("template_jinja_examples/index.html", name=name))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

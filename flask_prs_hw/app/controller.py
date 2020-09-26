from app import app
from flask import render_template
from app.models.player import *
from app.models.prs import *

@app.route('/')
def hello_world():
    return "Hello World"


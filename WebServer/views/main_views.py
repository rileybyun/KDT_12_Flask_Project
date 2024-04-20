from flask import Blueprint, render_template, request 
from datetime import datetime

bp = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/")

@bp.route('/')
def index():
    return render_template('index.html')
    
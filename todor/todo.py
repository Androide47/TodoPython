from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def index():
    return 'todo list'

@bp.route('/create')
def create():
    return 'create list'
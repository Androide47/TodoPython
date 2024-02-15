from flask import (Blueprint, render_template, request, url_for, flash, redirect)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/inicio')
def inicio():
    return render_template('auth/login.html')
@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username, generate_password_hash(password))
        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.inicio'))
        else:
            flash('El usuario ya existe')
            return redirect(url_for('auth.registro'))
        
        
    return render_template('auth/registro.html')
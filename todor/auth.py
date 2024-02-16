from flask import (Blueprint, render_template, request, url_for, flash, redirect, session, g)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/inicio', methods = ['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None
        
        user = User.query.filter_by(username = username).first()
        if user == None:
            error = 'El nombre de usuario o contraseña es incorrecto'
            
        elif not check_password_hash(user.password, password):
            error = 'El nombre de usuario o contraseña es incorrecto'
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
        
        flash(error)
        
    return render_template('auth/login.html')
@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username, generate_password_hash(password))
        
        
        error = None
        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.inicio'))
        else:
            error = f'El usuario {username} ya existe'
            flash('El usuario ya existe')
            return redirect(url_for('auth.registro'))
        
        
    return render_template('auth/registro.html')
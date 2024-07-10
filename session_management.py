from flask import session
from datetime import timedelta

def create_session(user_id):
    session['user_id'] = user_id
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

def update_session(user_id):
    session['user_id'] = user_id

def delete_session():
    session.pop('user_id', None)

def is_session_active():
    return 'user_id' in session

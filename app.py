from flask import Flask, redirect, url_for, session, render_template, request, jsonify
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from models import User
from session_management import create_session, update_session, delete_session, is_session_active
from error_handling import register_error_handlers

app = Flask(__name__)
app.secret_key = 'random_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
oauth = OAuth(app)

# OAuth2 provider configuration
oauth.register(
    name='github',
    client_id='YOUR_GITHUB_CLIENT_ID',
    client_secret='YOUR_GITHUB_CLIENT_SECRET',
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5000/callback',
    client_kwargs={'scope': 'user:email'}
)

register_error_handlers(app)

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)

@app.route('/callback')
def authorize():
    token = oauth.github.authorize_access_token()
    user_info = oauth.github.get('user', token=token).json()
    user = User.query.filter_by(username=user_info['login']).first()
    if not user:
        user = User(username=user_info['login'], email=user_info['email'])
        db.session.add(user)
        db.session.commit()
    create_session(user.id)
    return redirect('/')

@app.route('/logout')
def logout():
    delete_session()
    return redirect('/')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat_post():
    user_input = request.form['user_input']
    # Mock response from generative AI
    ai_response = f"Mock response to '{user_input}'"
    return jsonify({'user_input': user_input, 'ai_response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)

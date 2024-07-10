from flask import Flask, redirect, url_for, session, render_template, request, jsonify
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'random_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
oauth = OAuth(app)

# OAuth2 provider configuration
oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5000/callback',
    client_kwargs={'scope': 'openid profile email'}
)

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/callback')
def authorize():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session['user'] = user
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

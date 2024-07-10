import unittest
from app import app, db, User
from flask import session
from werkzeug.security import generate_password_hash
from error_handling import AuthenticationError, InvalidSessionError

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

        # Create a test user
        self.test_user = User(username='testuser', email='test@example.com')
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_successful_login(self):
        response = self.app.post('/login/github', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)
        self.assertIn('user_id', session)

    def test_failed_login(self):
        response = self.app.post('/login/github', follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Authentication failed', response.data)
        self.assertNotIn('user_id', session)

    def test_user_model_validation(self):
        user = User(username='newuser', email='new@example.com')
        db.session.add(user)
        db.session.commit()
        retrieved_user = User.query.filter_by(username='newuser').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'new@example.com')

    def test_session_management(self):
        with self.app:
            self.app.post('/login/github', follow_redirects=True)
            self.assertTrue('user_id' in session)
            self.app.get('/logout', follow_redirects=True)
            self.assertFalse('user_id' in session)

    def test_error_handling(self):
        with self.app:
            @app.route('/raise_auth_error')
            def raise_auth_error():
                raise AuthenticationError('Test authentication error')

            @app.route('/raise_session_error')
            def raise_session_error():
                raise InvalidSessionError('Test session error')

            response = self.app.get('/raise_auth_error')
            self.assertEqual(response.status_code, 401)
            self.assertIn(b'Authentication failed', response.data)

            response = self.app.get('/raise_session_error')
            self.assertEqual(response.status_code, 403)
            self.assertIn(b'Invalid session', response.data)

    def test_successful_registration(self):
        response = self.app.post('/register/github', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)
        self.assertIn('user_id', session)

    def test_failed_registration(self):
        response = self.app.post('/register/github', follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Authentication failed', response.data)
        self.assertNotIn('user_id', session)

if __name__ == '__main__':
    unittest.main()

import unittest
from app import app, db, User
from flask import session
from werkzeug.security import generate_password_hash

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

        # Create a test user
        self.test_user = User(username='testuser', email='test@example.com', password_hash=generate_password_hash('password'))
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_successful_login(self):
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)
        self.assertIn('user_id', session)

    def test_failed_login(self):
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='wrongpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Authentication failed', response.data)
        self.assertNotIn('user_id', session)

    def test_user_model_validation(self):
        user = User(username='newuser', email='new@example.com', password_hash=generate_password_hash('newpassword'))
        db.session.add(user)
        db.session.commit()
        retrieved_user = User.query.filter_by(username='newuser').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'new@example.com')

if __name__ == '__main__':
    unittest.main()

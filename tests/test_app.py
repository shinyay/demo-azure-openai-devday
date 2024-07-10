import pytest
from src.app import app, db
from src.models import Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Todo List' in response.data

def test_add_todo(client):
    response = client.post('/todos/add', data={'title': 'Test Todo', 'description': 'Test Description'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' in response.data

def test_edit_todo(client):
    todo = Todo(title='Test Todo', description='Test Description')
    db.session.add(todo)
    db.session.commit()
    response = client.post(f'/todos/edit/{todo.id}', data={'title': 'Updated Todo', 'description': 'Updated Description', 'completed': 'y'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated Todo' in response.data

def test_delete_todo(client):
    todo = Todo(title='Test Todo', description='Test Description')
    db.session.add(todo)
    db.session.commit()
    response = client.post(f'/todos/delete/{todo.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' not in response.data

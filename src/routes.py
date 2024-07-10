from flask import Blueprint, request, redirect, url_for, render_template
from src.models import db, Todo

bp = Blueprint('todo', __name__)

@bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@bp.route('/todos/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('todo.get_todos'))
    return render_template('add.html')

@bp.route('/todos/edit/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.completed = 'completed' in request.form
        db.session.commit()
        return redirect(url_for('todo.get_todos'))
    return render_template('edit.html', todo=todo)

@bp.route('/todos/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.get_todos'))

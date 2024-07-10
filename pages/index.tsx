import React, { useContext, useEffect, useState } from 'react';
import { TodoContext } from '../context/TodoContext';

const Index = () => {
  const { todos, addTodo, editTodo, deleteTodo, toggleTodo } = useContext(TodoContext);
  const [newTodo, setNewTodo] = useState('');
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    // Fetch todos from the backend
    fetch('/api/todos')
      .then((response) => response.json())
      .then((data) => {
        data.todos.forEach((todo) => addTodo(todo));
      });
  }, [addTodo]);

  const handleAddTodo = () => {
    if (newTodo.trim() === '') return;

    const todo = { id: Date.now(), text: newTodo, completed: false };
    addTodo(todo);
    setNewTodo('');

    // Persist the new todo to the backend
    fetch('/api/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(todo),
    });
  };

  const handleEditTodo = (id, newText) => {
    editTodo(id, newText);

    // Persist the updated todo to the backend
    fetch(`/api/todos/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: newText }),
    });
  };

  const handleDeleteTodo = (id) => {
    deleteTodo(id);

    // Delete the todo from the backend
    fetch(`/api/todos/${id}`, {
      method: 'DELETE',
    });
  };

  const handleToggleTodo = (id) => {
    toggleTodo(id);

    // Persist the updated todo to the backend
    fetch(`/api/todos/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: !todo.completed }),
    });
  };

  const filteredTodos = todos.filter((todo) => {
    if (filter === 'all') return true;
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
  });

  return (
    <div>
      <h1>Todo List</h1>
      <input
        type="text"
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="Add a new todo"
      />
      <button onClick={handleAddTodo}>Add</button>
      <div>
        <button onClick={() => setFilter('all')}>All</button>
        <button onClick={() => setFilter('active')}>Active</button>
        <button onClick={() => setFilter('completed')}>Completed</button>
      </div>
      <ul>
        {filteredTodos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => handleToggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => handleEditTodo(todo.id, prompt('Edit todo:', todo.text))}>Edit</button>
            <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Index;

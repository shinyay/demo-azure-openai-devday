# My Next.js App

This is a Next.js application created using the Next.js framework.

## Project Structure

The project has the following files and directories:

- `pages/api/hello.js`: This file is an API route that exports a function `hello` which handles the `/api/hello` endpoint.

- `pages/_app.js`: This file is a Next.js special file that exports a component `App` which is the root component of the application. It allows you to override the default App component provided by Next.js and customize the initialization of pages.

- `pages/index.js`: This file is a Next.js page component that exports a component `Index` which represents the home page of the application.

- `public/favicon.ico`: This file is the favicon for the application.

- `public/vercel.svg`: This file is an SVG image used by the application.

- `styles/Home.module.css`: This file contains CSS styles specific to the `Index` component.

- `styles/globals.css`: This file contains global CSS styles that are applied to all components.

- `.eslintrc.json`: This file is the configuration file for ESLint, a popular JavaScript linter. It specifies the rules and settings for linting the project.

- `next.config.js`: This file is the configuration file for Next.js. It allows you to customize various aspects of the Next.js build process and runtime behavior.

- `package.json`: This file is the configuration file for npm. It lists the dependencies and scripts for the project.

- `README.md`: This file contains the documentation for the project.

- `context/TodoContext.tsx`: This file defines the `TodoContext` and `TodoProvider` for state management using React Context API.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install the dependencies: `npm install`
3. Start the development server: `npm run dev`

## Using the Todo Application with Context

The Todo application uses React Context API for state management. The `TodoContext` and `TodoProvider` are defined in `context/TodoContext.tsx`. The context provides functions for adding, editing, deleting, and toggling todos.

To use the Todo application with context, follow these steps:

1. Wrap your application with the `TodoProvider` in `pages/_app.tsx`:

```tsx
import { TodoProvider } from '../context/TodoContext';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <TodoProvider>
      <Component {...pageProps} />
    </TodoProvider>
  );
}

export default MyApp;
```

2. Use the context functions in your components to manage todos. For example, in `pages/index.tsx`:

```tsx
import React, { useContext, useState } from 'react';
import { TodoContext } from '../context/TodoContext';

const Index = () => {
  const { todos, addTodo, editTodo, deleteTodo, toggleTodo } = useContext(TodoContext);
  const [newTodo, setNewTodo] = useState('');

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
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => editTodo(todo.id, prompt('Edit todo:', todo.text))}>Edit</button>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Index;
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

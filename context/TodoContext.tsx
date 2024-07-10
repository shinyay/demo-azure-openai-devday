import React, { createContext, useReducer, ReactNode } from 'react';

interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

type Action =
  | { type: 'ADD_TODO'; payload: Todo }
  | { type: 'EDIT_TODO'; payload: { id: number; text: string } }
  | { type: 'DELETE_TODO'; payload: { id: number } }
  | { type: 'TOGGLE_TODO'; payload: { id: number } };

interface TodoContextProps {
  todos: Todo[];
  addTodo: (todo: Todo) => void;
  editTodo: (id: number, text: string) => void;
  deleteTodo: (id: number) => void;
  toggleTodo: (id: number) => void;
}

const TodoContext = createContext<TodoContextProps | undefined>(undefined);

const todoReducer = (state: Todo[], action: Action): Todo[] => {
  switch (action.type) {
    case 'ADD_TODO':
      return [...state, action.payload];
    case 'EDIT_TODO':
      return state.map((todo) =>
        todo.id === action.payload.id ? { ...todo, text: action.payload.text } : todo
      );
    case 'DELETE_TODO':
      return state.filter((todo) => todo.id !== action.payload.id);
    case 'TOGGLE_TODO':
      return state.map((todo) =>
        todo.id === action.payload.id ? { ...todo, completed: !todo.completed } : todo
      );
    default:
      return state;
  }
};

const TodoProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [todos, dispatch] = useReducer(todoReducer, []);

  const addTodo = (todo: Todo) => dispatch({ type: 'ADD_TODO', payload: todo });
  const editTodo = (id: number, text: string) => dispatch({ type: 'EDIT_TODO', payload: { id, text } });
  const deleteTodo = (id: number) => dispatch({ type: 'DELETE_TODO', payload: { id } });
  const toggleTodo = (id: number) => dispatch({ type: 'TOGGLE_TODO', payload: { id } });

  return (
    <TodoContext.Provider value={{ todos, addTodo, editTodo, deleteTodo, toggleTodo }}>
      {children}
    </TodoContext.Provider>
  );
};

export { TodoContext, TodoProvider };

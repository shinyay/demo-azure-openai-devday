import { NextApiRequest, NextApiResponse } from 'next';

let todos = [
  { id: 1, text: 'Learn Next.js', completed: false },
  { id: 2, text: 'Build a Todo App', completed: false },
];

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  switch (req.method) {
    case 'GET':
      res.status(200).json({ todos });
      break;
    case 'POST':
      const newTodo = req.body;
      todos.push(newTodo);
      res.status(201).json(newTodo);
      break;
    case 'PUT':
      const { id, text, completed } = req.body;
      todos = todos.map((todo) =>
        todo.id === id ? { ...todo, text, completed } : todo
      );
      res.status(200).json({ id, text, completed });
      break;
    case 'DELETE':
      const { id: deleteId } = req.body;
      todos = todos.filter((todo) => todo.id !== deleteId);
      res.status(204).end();
      break;
    default:
      res.setHeader('Allow', ['GET', 'POST', 'PUT', 'DELETE']);
      res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}

import React from 'react';
import { Checkbox } from '@/components/ui/checkbox';
import { Button } from '@/components/ui/button';

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <li className="flex items-center space-x-2">
      <Checkbox
        checked={todo.completed}
        onCheckedChange={(checked) => onToggle(todo.id, checked as boolean)}
      />
      <span className={todo.completed ? 'line-through' : ''}>{todo.title}</span>
      <Button variant="destructive" onClick={() => onDelete(todo.id)}>Delete</Button>
    </li>
  );
};

export default TodoItem;
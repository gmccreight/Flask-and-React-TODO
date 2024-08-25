import React from 'react';
import * as Checkbox from '@radix-ui/react-checkbox';
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Todo } from '@/types/todo';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <li className="flex items-center space-x-2 py-2">
      <Checkbox.Root
        className="flex h-4 w-4 items-center justify-center rounded border border-primary"
        checked={todo.completed}
        onCheckedChange={(checked: boolean) => onToggle(todo.id, checked)}
      >
        <Checkbox.Indicator className="text-primary">
          ✓
        </Checkbox.Indicator>
      </Checkbox.Root>
      <span className={cn("flex-grow", todo.completed && "line-through")}>{todo.title}</span>
      <Button variant="destructive" size="sm" onClick={() => onDelete(todo.id)}>Delete</Button>
    </li>
  );
};

export default TodoItem;
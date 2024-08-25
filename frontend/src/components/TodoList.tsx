import React from 'react';
import { Todo } from '../types/todo';
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import * as Checkbox from '@radix-ui/react-checkbox';

interface TodoListProps {
  todos: Todo[];
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}

const TodoList: React.FC<TodoListProps> = ({ todos, onToggle, onDelete }) => {
  return (
    <div className="space-y-4">
      {todos.map((todo) => (
        <Card key={todo.id}>
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Checkbox.Root
                className="flex h-4 w-4 items-center justify-center rounded border border-primary"
                checked={todo.completed}
                onCheckedChange={() => onToggle(todo.id, !todo.completed)}
              >
                <Checkbox.Indicator className="text-primary">
                  ✓
                </Checkbox.Indicator>
              </Checkbox.Root>
              <span className={todo.completed ? 'line-through' : ''}>{todo.title}</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            {/* You can add more details about the todo here if needed */}
          </CardContent>
          <CardFooter>
            <Button variant="destructive" onClick={() => onDelete(todo.id)}>Delete</Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
};

export default TodoList;
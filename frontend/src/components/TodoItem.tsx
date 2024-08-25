import React from 'react';
import * as Checkbox from '@radix-ui/react-checkbox';
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Todo } from '@/types/todo';
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card";

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <Card className="bg-slate-50 shadow-md">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Checkbox.Root
            className="flex h-4 w-4 items-center justify-center rounded border border-primary"
            checked={todo.completed}
            onCheckedChange={(checked: boolean) => onToggle(todo.id, checked)}
          >
            <Checkbox.Indicator className="text-primary">
              ✓
            </Checkbox.Indicator>
          </Checkbox.Root>
          <span className={cn(todo.completed && "line-through")}>{todo.title}</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        {/* You can add more details about the todo here if needed */}
      </CardContent>
      <CardFooter>
        <Button variant="destructive" onClick={() => onDelete(todo.id)}>Delete</Button>
      </CardFooter>
    </Card>
  );
};

export default TodoItem;
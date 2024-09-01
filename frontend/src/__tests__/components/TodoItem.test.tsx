import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import TodoItem from '../../components/TodoItem';

jest.mock('@radix-ui/react-checkbox');

describe('TodoItem', () => {
  const mockTodo = {
    id: 1,
    title: 'Test Todo',
    completed: false,
  };

  const mockOnToggle = jest.fn();
  const mockOnDelete = jest.fn();

  it('shows checkbox indicator when clicked', () => {
    render(
      <TodoItem
        todo={mockTodo}
        onToggle={mockOnToggle}
        onDelete={mockOnDelete}
      />
    );

    const checkbox = screen.getByRole('checkbox');
    expect(checkbox).not.toHaveAttribute('data-state', 'checked');

    fireEvent.click(checkbox);

    expect(mockOnToggle).toHaveBeenCalledWith(1, true);
  });
});
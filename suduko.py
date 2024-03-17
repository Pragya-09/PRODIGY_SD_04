import tkinter as tk

def solve_sudoku():
    # Convert the input grid into a 2D list
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = entry_cells[i][j].get()
            if cell_value == "":
                row.append(0)
            else:
                row.append(int(cell_value))
        grid.append(row)
    
    # Solve the Sudoku puzzle
    if solve_sudoku_recursive(grid):
        # Display the solved puzzle
        for i in range(9):
            for j in range(9):
                entry_cells[i][j].delete(0, tk.END)
                entry_cells[i][j].insert(0, str(grid[i][j]))
    else:
        result_label.config(text="No solution exists for this puzzle.")

def solve_sudoku_recursive(grid):
    # Find the next empty cell
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Puzzle is solved
    
    row, col = empty_cell
    
    # Try filling the empty cell with digits 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            
            # Recursively solve the puzzle
            if solve_sudoku_recursive(grid):
                return True
            
            # If no solution found, backtrack
            grid[row][col] = 0
    
    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # Check if num is not already present in the row
    if num in grid[row]:
        return False
    
    # Check if num is not already present in the column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check if num is not already present in the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True

# Create main window
window = tk.Tk()
window.title("Sudoku Solver")

# Sudoku grid input
entry_cells = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(window, width=3)
        entry.grid(row=i, column=j, padx=1, pady=1)
        row_entries.append(entry)
    entry_cells.append(row_entries)

# Solve button
solve_button = tk.Button(window, text="Solve Sudoku", command=solve_sudoku)
solve_button.grid(row=9, columnspan=9, pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=10, columnspan=9)

window.mainloop()

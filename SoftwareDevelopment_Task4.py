import tkinter as tk
from tkinter import messagebox

# Function to check if a number can be placed in a cell
def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Backtracking function to solve Sudoku
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Function 
def solve():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            if value == "":
                row.append(0)
            else:
                try:
                    value = int(value)
                    if value < 1 or value > 9:
                        raise ValueError
                    row.append(value)
                except ValueError:
                    messagebox.showerror("Invalid Input", f"Invalid number at row {i + 1}, column {j + 1}.")
                    return
        grid.append(row)

    if solve_sudoku(grid):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(grid[i][j]))
        messagebox.showinfo("Success", "Sudoku solved successfully!")
    else:
        messagebox.showerror("Error", "This Sudoku puzzle cannot be solved.")

# Function 
def clear_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entries = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5, ipady=5)
        if (i // 3 + j // 3)% 2 == 0:
            entry.config(bg="#f0f0f0")  # Alternating background for better visibility
        row.append(entry)
    entries.append(row)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

solve_button = tk.Button(button_frame, text="Solve", command=solve, width=10, bg="green", fg="white")
solve_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_grid, width=10, bg="red", fg="white")
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()
        
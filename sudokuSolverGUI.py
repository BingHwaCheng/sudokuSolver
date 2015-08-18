# sudokuSolverGUI: GUI interface for sudoku solver

# Copyright (c) 2015 Bing Hwa Cheng

from Tkinter import *
from sudokuSolver import *

"""
# default puzzle
init_state = [ [ 8, 5,-1,-1, 3,-1, 7,-1,-1], 
               [-1,-1, 4, 8,-1,-1,-1, 5,-1], 
               [ 6,-1, 7,-1, 4, 9, 3, 8,-1], 
               [-1,-1,-1, 9,-1,-1, 4,-1, 1], 
               [ 9,-1, 5,-1,-1,-1, 2,-1, 8], 
               [ 1,-1, 8,-1,-1, 7,-1,-1,-1], 
               [-1, 8, 9, 3, 2,-1, 6,-1, 5], 
               [-1, 2,-1,-1,-1, 6, 9,-1,-1], 
               [-1,-1, 1,-1, 9,-1,-1, 2, 3] ]
"""

# evil example 
init_state = [ [-1, 6, 3,-1,-1, 7,-1,-1, 4], 
               [ 8, 7,-1, 5,-1,-1,-1, 3,-1], 
               [-1, 9,-1, 1,-1,-1,-1,-1,-1], 
               [-1,-1, 9, 7,-1,-1,-1,-1,-1], 
               [-1, 5,-1,-1,-1,-1,-1, 7,-1], 
               [-1,-1,-1,-1,-1, 5, 9,-1,-1], 
               [-1,-1,-1,-1,-1, 4,-1, 2,-1], 
               [-1, 8,-1,-1,-1, 6,-1, 4, 7], 
               [ 4,-1,-1, 9,-1,-1, 8, 1,-1] ];
"""
# expert example
init_state = [ [-1, 4,-1,-1, 5,-1,-1,-1, 7], 
               [-1,-1, 3, 7,-1, 8,-1, 1,-1],
               [ 5,-1,-1,-1,-1,-1,-1,-1,-1],
               [-1,-1, 8, 6, 1,-1,-1,-1,-1],
               [-1,-1, 7,-1,-1,-1,-1, 4, 2],
               [-1,-1,-1,-1, 3,-1,-1,-1, 6],
               [-1, 5,-1,-1,-1,-1,-1,-1,-1],
               [ 7,-1,-1,-1, 4,-1,-1,-1, 8],
               [-1,-1, 2, 1,-1,-1, 7, 6,-1] ]
"""  
  
# -------------------------------------------------
# GUI handler function for "solve"
# -------------------------------------------------
def solve():
    global init_state
    row_cnt = 0
    for row in rows:
        col_cnt = 0
        for col in row:
            if col.get() == "":
                val = -1
            else: 
                val = col.get()
            init_state[row_cnt][col_cnt] = int(val)
            col_cnt = col_cnt + 1
        row_cnt = row_cnt + 1

    ss = sudokuSolver(init_state)
    ss.backtrackingSearch()
    redrawGrid(ss.getCurrState())

def redrawGrid(curr_state):
    global init_state
    row_cnt = 0
    for row in rows:
        col_cnt = 0
        for col in row:
            col.delete(0)
            col.insert(END, curr_state[row_cnt][col_cnt])
            col_cnt = col_cnt + 1
        row_cnt = row_cnt + 1
# -------------------------------------------------
# GUI main function
# -------------------------------------------------
# top frame: 9x9 grids
rows = []
for i in range(9):
    cols = []
    for j in range(9):
        e = Entry(relief=RIDGE, width=2)
        e.grid(row=i, column=j, sticky=NSEW)
        
        val = ""
        if init_state[i][j] > 0:
            val = init_state[i][j]
            
        e.insert(END, val)
        cols.append(e)
    rows.append(cols)


# bottom frame: button
Button(text='SOLVE', command=solve).grid(columnspan=10)
mainloop()


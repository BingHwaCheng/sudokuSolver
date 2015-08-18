# sudokuSolver: use backtracking search algorithm to solve sudoku puzzle

# Copyright (c) 2015 Bing Hwa Cheng

class sudokuSolver:
    curr_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    assignment_cnt = 0
    revert_cnt = 0


    # --------------------------------------------------------
    # Initialization, copy the 9x9 array from GUI input
    # --------------------------------------------------------
    def __init__(self,init_state):
        for i in range(9):
            for j in range(9):
                self.curr_state[i][j] = init_state[i][j]
                print self.curr_state[i][j],
            print
    
    # --------------------------------------------------------
    # Backtracking calls
    # --------------------------------------------------------
    def backtrackingSearch(self):
        self.recursiveBacktracking()
    
    
    # --------------------------------------------------------
    # Recursive backtracking calls
    # --------------------------------------------------------
    def recursiveBacktracking(self):
    
        # get unassigned entry
        uGrid = self.getUnassignedGrid();
        if uGrid[0] == -1:
            print "Assignment complete"
            print "assignment_cnt = " + str(self.assignment_cnt)
            print "revert_cnt = " + str(self.revert_cnt)
            self.printCurrState()
            return 1
            
        # get possible values of this unassigned entry
        possibleValues = self.getPossibleValues(uGrid)
    
        for i in range(9):
            if possibleValues[i] == 1:
                val = i+1
                self.assignment_cnt = self.assignment_cnt + 1
                
                if self.checkConsistency(uGrid, val) == 1:
                    self.curr_state[uGrid[0]][uGrid[1]] = val
                    
                    if self.recursiveBacktracking() == 1:
                        return 1
                    else:
                        # remove assignment
                        self.curr_state[uGrid[0]][uGrid[1]] = -1
                        self.revert_cnt = self.revert_cnt + 1
        
        return 0
    
    
    # --------------------------------------------------------
    # Check for consistency
    # --------------------------------------------------------
    def checkConsistency(self, uGrid, val):
        # check for column
        for i in range(9):
            if i != uGrid[0] and self.curr_state[i][uGrid[1]] == val:
                return 0
        
        # check for row
        for i in range(9):
            if i != uGrid[1] and self.curr_state[uGrid[0]][i] == val:
                return 0
                
        # check for 3x3 grid
        x_base = 3*(uGrid[0]/3)
        y_base = 3*(uGrid[1]/3)        
        for i in range(x_base, x_base+3):
            for j in range(y_base, y_base+3):
                if i != uGrid[0] and j != uGrid[1] and self.curr_state[i][j] == val:
                    return 1
        
        return 1
    
    
    # --------------------------------------------------------
    # Get possible values for a given grid
    # possibleValues is an array of 9.
    # Value of 1 in entry x means x+1 is a possible value
    # --------------------------------------------------------
    def getPossibleValues(self, uGrid):
    
        # initialize possibleValues to all 1's
        possibleValues = []
        for i in range(9):
            possibleValues.append(1)
            
        # first check for row and column (non-repeating)
        for i in range(9):
            val = self.curr_state[uGrid[0]][i]
            if val > 0:
                possibleValues[val-1] = 0
            val = self.curr_state[i][uGrid[1]]
            if val > 0:
                possibleValues[val-1] = 0
 
        # then check for numbers in 3x3 grid
        x_base = 3*(uGrid[0]/3)
        y_base = 3*(uGrid[1]/3)        
        for i in range(x_base, x_base+3):
            for j in range(y_base, y_base+3):
                val = self.curr_state[i][j]
                if val> 0:
                    possibleValues[val-1] = 0
        
        return possibleValues
        
    # --------------------------------------------------------
    # Get unassigned entry (value = -1)
    # --------------------------------------------------------
    def getUnassignedGrid(self):
        for i in range(9):
            for j in range(9):
                if self.curr_state[i][j] == -1:
                    return [i,j]
        
        # if all entries are completed, return -1
        return [-1,-1]
    
    # --------------------------------------------------------
    # Print curr_state
    # --------------------------------------------------------
    def printCurrState(self):
        print "curr_state:"
        for i in range(9):
            for j in range(9):
                print self.curr_state[i][j],
            print
    
    # --------------------------------------------------------
    # Get curr_state
    # --------------------------------------------------------
    def getCurrState(self):
        return self.curr_state
    
        
    
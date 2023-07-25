"""
This class represents a Sudoku board object. A Sudoku board contains 81 cells.
Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""


import cell


selected_cell = None


class Board:
    """
    Initializes a new Sudoku board object.
    """
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = ["", "", "", "", "", "", "", "", ""] * 9

    '''
    Marks the cell at (row, col) in the board as the current selected cell.
    A Board object has 81 Cell objects. ---> 9 x 9 
    '''
    def select(self, row, col):
        row_num = row   #not sure if self.width and self.height should be ultized instead.
        col_num = col
      
        selected_cell = self.board[row_num][col_num]

        #Once a cell has been selected, the user can edit its value or sketched value. 
        return selected_cell

    """
    If a tuple of (x,y) coordinates is within the displayed board,
    this function returns a tuple of the (row,col) of the cell which
    was clicked. Otherwise, the function returns None.
    """
    def click(self, x, y):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            return None
        else:
            row = x // (self.width / 9)
            col = y // (self.height / 9)
            return (row, col)
        
    '''
    Sets the sketched value of the current selected cell equal to user entered value.
    It will be displayed at the top left corner of the cell using the draw() function. 
    '''
    def sketch(self,value):
        pass

    """
    Sets the value of the current selected cell equal to user-entered
    value. Called when user presses the Enter key.
    """
    def place_number(self, value):
        if selected_cell is not None:
            selected_cell.set_cell_value(value)


    '''
    Returns a Boolean value indicating whether the board is full or not. 
    '''
    def is_full(self):
        pass

    """
    Updates the underlying 2D board with the values in all cells.
    """
    def update_board(self):
        for cell in self.board:
            if cell.value != cell.sketched_value:
                cell.value = cell.sketched_value

    '''
    Check whether the Sudoku board is solved correctly
    '''
    def check_board(self):
        pass

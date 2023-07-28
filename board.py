"""
This class represents a Sudoku board object. A Sudoku board contains 81 cells.
Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""


import cell
from constants import *



class Board:
    """
    Initializes a new Sudoku board object.
    """
    def __init__(self, width, height, screen, difficulty, selected_cell):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = selected_cell
        self.board = ["", "", "", "", "", "", "", "", ""] * 9
    """
    Draws an outline of the Sudoku grid, with bold lines to delineate the 3 x 3 boxes.
    Draws every cell on the board
    """
    def draw(self):
        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            if i % 3 = 0: # if i %3 is 0 then its at place 0, 3, 6 and 9, the spots for bold lines
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    MAIN_LINE_WIDTH
                )
            else: # else, print normal line width
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
        # draw vertical lines
        for i in range(1, BOARD_COLS):
            if i % 3 = 0:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    MAIN_LINE_WIDTH
                )
            else:   
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    LINE_WIDTH
                )
    
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
    Clears the value cell. Note that the user can only remove the cell values 
    and sketched value that are filled by themselves.
    '''
    def clear(self):
        # if the cell is an editable cell
            # self.value = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] is #FIXME 
                : '''establish editable cell vs uneditable cell'''
            self.value = 0
    
    '''
    Sets the sketched value of the current selected cell equal to user entered value.
    It will be displayed at the top left corner of the cell using the draw() function. 
    '''
    def sketch(self,value):
        self.selected_cell = value
        # draw the new value(?)

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
        counter = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    counter += 1
        if counter > 0:
            return False
        else:
            return True

    '''
    Reset all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    '''
    def reset_to_original(self):
        board = self.original_board
        return board
    
    """
    Updates the underlying 2D board with the values in all cells.
    """
    def update_board(self):
        for cell in self.board:
            if cell.value != cell.sketched_value:
                cell.value = cell.sketched_value

    '''
    Find an empty cell and returns it's row and col as a tuple (x,y)
    '''
    def find_empty(self):
        pass
        
    '''
    Check whether the Sudoku board is solved correctly
    '''
    def check_board(self):
        pass

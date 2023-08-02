"""
This class represents a Sudoku board object. A Sudoku board contains 81 cells.

Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""


import pygame
from cell import *
from sudoku_generator import *
from constants import *


class Board:
    """
    Initializes a new Sudoku board object containing underlying cell objects.
    """
    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        if difficulty == "easy":
            self.board = generate_sudoku(9, 30)
        elif difficulty == "medium":
            self.board = generate_sudoku(9, 40)
        elif difficulty == "hard":
            self.board = generate_sudoku(9, 50)
        self.original_board = self.board.copy()
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(cols)]
            for i in range(rows)
        ]

    """
    Draws an outline of the Sudoku grid, with bold lines to delineate the 3 x 3 board boxes.
    Lighter lines delineate the 9 x 9 cell boxes.
    Draws every cell on the board.
    """
    def draw(self):
        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            if i % 3 == 0:  # if i %3 is 0 then it's at place 0, 3, 6 and 9, the spots for bold lines
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    MAIN_LINE_WIDTH
                )
            else:  # else, print normal line width
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR_GRAY,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
        # draw vertical lines
        for i in range(1, BOARD_COLS):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT), 
                    MAIN_LINE_WIDTH
                )
            else:   
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR_GRAY,  # originally LINE_COLOR (color black)
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    LINE_WIDTH
                )
    
    """
    Marks the cell at (row, col) in the board as the current selected cell.
    """
    def select(self, row, col):
        for cell in self.cells:
            if cell.is_selected:
                cell.is_selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.is_selected = True

    """
    If a tuple of (x,y) coordinates is within the displayed board,
    this function returns a tuple of the (row,col) of the cell which
    was clicked. Otherwise, the function returns None.
    """
    def click(self, x, y):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            return None
        else:
            row = x // (self.width / self.rows)
            col = y // ((self.height - 100) / self.rows)
            return row, col

    """
    Clears the selected cell. Note that the user can only remove the cell values 
    and sketched value that are filled by themselves.
    """
    def clear(self):
        if self.selected_cell is not None and self.selected_cell.is_editable:
            self.selected_cell.value = 0
            self.selected_cell.sketched_value = 0

    """
    Sets the sketched value of the current selected cell equal to user entered value.
    It will be displayed at the top left corner of the cell using the draw() function. 
    """
    def sketch(self, sketched_value):
        if self.selected_cell is not None and self.selected_cell.is_editable:
            if sketched_value in range(1, 10):
                self.selected_cell.sketched_value = sketched_value

    """
    Sets the value of the current selected cell equal to user-entered
    value. Called when user presses the Enter key.
    """
    def place_number(self, value):
        if self.selected_cell is not None and self.selected_cell.is_editable:
            if value in range(1, 10):
                self.selected_cell.value = value

    """
    Returns a Boolean value indicating whether the board is full or not. 
    """
    def is_full(self):
        for row in self.board:
            for number in row:
                if number == 0:   # 0 represents empty spaces
                    return False  # means the board is not full yet
        return True  # True when board completely full.

    """
    Reset all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    """
    def reset_to_original(self):
        self.board = self.original_board
    
    """
    Updates the underlying 2D board with the values in all cells.
    """
    def update_board(self):
        for cell in self.board:
            if cell.value != cell.sketched_value:
                cell.value = cell.sketched_value

    """
    Find an empty cell and returns it's row and col as a tuple (x,y)
    """
    def find_empty(self):
        # FIXME
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return_tuple = (i, j)
                    return return_tuple
                else:
                    return None
        
    """
    Checks whether the Sudoku board is solved correctly.
    """
    def check_board(self):
        # board is solved correctly if each digit (1-9) only appear once in every row/col
        for row in range(9):
            if self.board[row][0] != self.board[row][1] != self.board[row][2] != self.board[row][3] != self.board[row][4] != self.board[row][5] != self.board[row][6] != self.board[row][7] != self.board[row][8]:
                return True  # solved correctly

        for col in range(9):
            if self.board[0][col] != self.board[1][col] != self.board[2][col] != self.board[3][col] != self.board[4][col] != self.board[5][col] != self.board[6][col] != self.board[7][col] != self.board[8][col]:
                return True  # solved correctly

        return False  # not solved correctly

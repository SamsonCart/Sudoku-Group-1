"""
This class represents a Sudoku board object. A Sudoku board contains 81 cells.

Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""

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
            self.original_board = generate_sudoku(9, 30)
        elif difficulty == "medium":
            self.original_board = generate_sudoku(9, 40)
        elif difficulty == "hard":
            self.original_board = generate_sudoku(9, 50)
        self.cells = [
            [Cell(self.original_board[i][j], i, j, screen) for j in range(cols)]
            for i in range(rows)
        ]

    """
    Returns 2D list containing underlying cell values. Mainly for debugging purposes.
    """

    def get_board_list(self):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.cells[i][j].value)
            result.append(row)
        return result

    """
    Draws an outline of the Sudoku grid, with bold lines to delineate the 3 x 3 board boxes.
    Lighter lines delineate the 9 x 9 cell boxes.
    Draws every cell on the board.
    """

    '''
    Draw_grid function draws the grid for the game board and is called into the board
    draw(self)'''

    def draw_grid(self):
        # draw top boarder
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (0, 0),
            (BOARD_ROWS * SQUARE_SIZE, 0),
            MAIN_LINE_WIDTH
        )

        # draw right boarder
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (BOARD_ROWS * SQUARE_SIZE, 0),
            (BOARD_ROWS * SQUARE_SIZE, BOARD_ROWS * SQUARE_SIZE),
            MAIN_LINE_WIDTH
        )

        # draw left boarder
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (0, 0),
            (0, BOARD_COLS * SQUARE_SIZE),
            MAIN_LINE_WIDTH
        )

        # draw bottom boarder
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (0, BOARD_COLS * SQUARE_SIZE),
            (BOARD_COLS * SQUARE_SIZE, BOARD_COLS * SQUARE_SIZE),
            MAIN_LINE_WIDTH
        )

        # draw horizontal lines
        for i in range(1, BOARD_ROWS + 1):
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
                    (i * SQUARE_SIZE, HEIGHT - 100),
                    MAIN_LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR_GRAY,  # originally LINE_COLOR (color black)
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT - 100),
                    LINE_WIDTH
                )

    def draw(self):
        # draws the grid
        self.draw_grid()

        # draw the cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw()  # pulls out each individual cell and runs it
                # through Cell.draw

    """
    Marks the cell at (row, col) in the board as the current selected cell.
    """

    def select(self, row, col, screen):
        self.draw_grid()
        for i in range(self.rows):
            for cell in self.cells[i]:
                if cell.is_selected:
                    cell.is_selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.is_selected = True
        if self.selected_cell.is_selected:
            for i in range(row, row + 2):  # range for x parameters
                pygame.draw.line(
                    screen,
                    SELECTED_COLOR,
                    (i * SQUARE_SIZE, col * SQUARE_SIZE),
                    (i * SQUARE_SIZE, (col + 1) * SQUARE_SIZE),
                    LINE_WIDTH
                )

            for i in range(col, col + 2):  # range for y parameters
                pygame.draw.line(
                    screen,
                    SELECTED_COLOR,
                    (row * SQUARE_SIZE, i * SQUARE_SIZE),
                    ((row + 1) * SQUARE_SIZE, i * SQUARE_SIZE),
                    LINE_WIDTH
                )

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
            row = int(row)
            col = int(col)
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
        self.selected_cell.erase_sketched_number()
        if self.selected_cell.is_editable and self.selected_cell.value is not None:
            if sketched_value in range(0, self.rows + 1):
                print(f"Sketch {sketched_value}")
                self.selected_cell.sketched_value = sketched_value
                print(f'selected cell sketched value is {self.selected_cell.sketched_value}')
                self.selected_cell.draw()

    """
    Sets the value of the current selected cell equal to user-entered
    value. Called when user presses the Enter key.
    """

    def place_number(self, value):
        if self.selected_cell.is_editable and self.selected_cell is not None:
            if value in range(1, self.rows + 1):
                self.selected_cell.value = value
                print(f"cell {value}")
                print(f'selected cell value is {self.selected_cell.value}')
                self.selected_cell.draw()
                self.selected_cell.erase_sketched_number()
                self.selected_cell.is_editable = False

    """
    Returns a Boolean value indicating whether the board is full or not. 
    """

    def is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return False
        return True

    """
    Reset all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    """

    def reset_to_original(self):
        self.selected_cell = None
        self.cells = [
            [Cell(self.original_board[i][j], i, j, self.screen) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    """
    Find an empty cell and returns its row and col as a tuple (x,y)
    """

    def find_empty(self):
        for i in range(self.rows):
            for cell in self.cells[i]:
                if cell.value == 0:
                    return cell.row, cell.col
        return None

    """
    Checks whether the Sudoku board is solved correctly by checking row, column, and box sums 
    as well as ensuring there are no duplicate numbers in each row, column or box.
    """

    def check_board(self):
        # check that row sum is equal to 45 for all 9 rows
        for i in range(self.rows):
            row_sum = 0
            for j in range(self.cols):
                row_sum += self.cells[i][j].value
            if row_sum != 45:
                return False

        # check that column sum is equal to 45 for all 9 columns
        for j in range(self.rows):
            col_sum = 0
            for i in range(self.cols):
                col_sum += self.cells[i][j].value
            if col_sum != 45:
                return False

        # check that box sum is equal to 45 for all 9 boxes
        for (row_start, col_start) in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            box_sum = 0
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    box_sum += self.cells[row_start + i][col_start + j].value
            if box_sum != 45:
                return False

        # make a list of values in a given row, compare the list to it's set
        for i in range(self.rows):
            row_values = []
            for j in range(self.cols):
                row_values.append(self.cells[i][j].value)  # FIXME check syntax
            if len(row_values) != len(set(row_values)):
                return False

        # make a list of values in a given col, compare the list to it's set
        for i in range(self.cols):
            col_values = []
            for j in range(self.rows):
                col_values.append(self.cells[i][j].value)  # FIXME check syntax
            if len(col_values) != len(set(col_values)):
                return False

        # make a list of values in a given box, compare the list to it's set
        for (row_start, col_start) in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            box_nums = []
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    box_nums.append(self.cells[row_start + i][col_start + j].value)
            if len(box_nums) != len(set(box_nums)):
                return False

        return True

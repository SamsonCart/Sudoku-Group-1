"""
This program generates an interactive Sudoku game.

Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""

import pygame
import sys
from constants import *
from board import Board


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    subtitle_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR_BLACK)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # initialize and draw subtitle
    subtitle_surface = subtitle_font.render("Select Game Mode:", 0, LINE_COLOR_BLACK)
    subtitle_rectangle = subtitle_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(subtitle_surface, subtitle_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("EASY", 0, (255, 255, 255))
    medium_text = button_font.render("MEDIUM", 0, (255, 255, 255))
    hard_text = button_font.render("HARD", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR_BLACK)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR_BLACK)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR_BLACK)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"  # Return easy removed cells value
                elif medium_rectangle.collidepoint(event.pos):
                    return "medium"  # return medium removed cells value
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"  # return hard removed cells value
        pygame.display.update()

#game over screen - not called yet
def draw_game_over(screen):
    # Initialize title font
    gameover_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR) #white background

    # Initialize and draw title
    gameover_title_surface = gameover_title_font.render("Game Over :(", 0, LINE_COLOR_BLACK)
    gameover_title_rectangle = gameover_title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(gameover_title_surface, gameover_title_rectangle)

    # Initialize button
    # Initialize text first
    restart_game_text = button_font.render("Restart", 0, (255, 255, 255))

    # Initialize button background color and text
    restart_game_surface = pygame.Surface((restart_game_text.get_size()[0] + 20, restart_game_text.get_size()[1] + 20))
    restart_game_surface.fill(LINE_COLOR_BLACK)
    restart_game_surface.blit(restart_game_text, (10, 10))

    # Initialize button rectangle
    restart_game_rectangle = restart_game_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    
    # Draw button
    screen.blit(restart_game_surface, restart_game_rectangle)

#game won screen - not called yet
def draw_game_won(screen):
    # Initialize title font
    gamewon_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR) #white background

    # Initialize and draw title
    gamewon_title_surface = gamewon_title_font.render("Game Won!", 0, LINE_COLOR_BLACK)
    gamewon_title_rectangle = gamewon_title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(gamewon_title_surface, gamewon_title_rectangle)

    # Initialize button
    # Initialize text first
    exit_game_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize button background color and text
    exit_game_surface = pygame.Surface((exit_game_text.get_size()[0] + 20, exit_game_text.get_size()[1] + 20))
    exit_game_surface.fill(LINE_COLOR_BLACK)
    exit_game_surface.blit(exit_game_text, (10, 10))

    # Initialize button rectangle
    exit_game_rectangle = exit_game_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    
    # Draw button
    screen.blit(exit_game_surface, exit_game_rectangle)


def initialize_buttons(screen):

    bottom_button_font = pygame.font.Font(None, 40)
    # Initialize buttons
    # Initialize text first
    reset_text = bottom_button_font.render("RESET", 0, (255, 255, 255))
    restart_text = bottom_button_font.render("RESTART", 0, (255, 255, 255))
    exit_text = bottom_button_font.render("EXIT", 0, (255, 255, 255))

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR_BLACK)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR_BLACK)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR_BLACK)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 450))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 450))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 450))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set width and height of board
    pygame.display.set_caption('Sudoku')  # window screen name


    difficulty = draw_game_start(screen)
    screen.fill(BG_COLOR_IN_GAME)  # Screen represents window screen(predetermined width and height from constants.py)

    game_board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, difficulty)
    game_board.draw(screen)

    bottom_button_font = pygame.font.Font(None, 40)
    # Initialize buttons
    # Initialize text first
    reset_text = bottom_button_font.render("RESET", 0, (255, 255, 255))
    restart_text = bottom_button_font.render("RESTART", 0, (255, 255, 255))
    exit_text = bottom_button_font.render("EXIT", 0, (255, 255, 255))

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR_BLACK)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR_BLACK)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR_BLACK)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 450))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 450))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 450))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

    while True:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~EVENT LOOP STARTS HERE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        for event in pygame.event.get():

            # -----------CLOSE WINDOW OPTION HERE ------------------
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # ------MOUSECLICK HERE---------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(x, y)
                if y <= 900:
                    row, col = game_board.click(x, y)
                    print(row, col)  # click method
                    game_board.select(row, col, screen)  # select method
                if y > 900:
                    if reset_rectangle.collidepoint(event.pos):
                        game_board.reset_to_original()
                        game_board.draw(screen)
                        initialize_buttons(screen)
                        for row in game_board.cells:
                            for cell in row:
                                cell.draw()
                    elif restart_rectangle.collidepoint(event.pos):
                        main()
                    elif exit_rectangle.collidepoint(event.pos):
                        sys.exit()
            if event.type == pygame.KEYDOWN and game_board.selected_cell.value == 0:
                if event.key == pygame.K_1:
                    game_board.sketch(1)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_2:
                    game_board.sketch(2)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_3:
                    game_board.sketch(3)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_4:
                    game_board.sketch(4)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_5:
                    game_board.sketch(5)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_6:
                    game_board.sketch(6)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_7:
                    game_board.sketch(7)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_8:
                    game_board.sketch(8)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_9:
                    game_board.sketch(9)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP1:
                    game_board.sketch(1)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP2:
                    game_board.sketch(2)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP3:
                    game_board.sketch(3)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP4:
                    game_board.sketch(4)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP5:
                    game_board.sketch(5)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP6:
                    game_board.sketch(6)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP7:
                    game_board.sketch(7)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP8:
                    game_board.sketch(8)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_KP9:
                    game_board.sketch(9)
                    print(game_board.selected_cell.row)
                    print(game_board.selected_cell.col)
                elif event.key == pygame.K_RETURN:
                    game_board.place_number(game_board.selected_cell.sketched_value)

                if game_board.is_full():  # THIS APPEARS TO WORK CORRECTLY
                    if game_board.check_board():
                        print("Yay, you win!")  # PLAYED GAME MULTIPLE TIMES & EVERY TIME I WON, RECEIVED THIS STATEMENT
                        break
                    else:
                        print("Sorry, you lose!")  # PLAYED GAME MULTIPLE TIMES & EVERY TIME I LOST, RECEIVED THIS STATEMENT
                        break

        pygame.display.update()

main()

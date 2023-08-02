"""
This program generates an interactive Sudoku game.

Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""

import pygame
from constants import *
from board import Board

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set width and height of board
pygame.display.set_caption('Sudoku') #window screen name

#======================INITIALIZE THE MAIN MENU / RETURN DIFFICULTY===========================

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

  #initalize and draw subtitle
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
          return "medium" # return medium removed cells value
        elif hard_rectangle.collidepoint(event.pos):
          return "hard" # return hard removed cells value
    pygame.display.update()

difficulty = draw_game_start(screen)
screen.fill(BG_COLOR_IN_GAME)  # Screen represents window screen(predetermined width and height from constants.py)

game_board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, difficulty) # creates a Board object
Board.draw(game_board)

#python3 sudoku.py
#FIXME Import remaining classes
from constants import *
#from board import *
import pygame
import sys

#initialize the game window and set the top bar caption
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Genorator")

#initalize a chip font variable
chip_font = pygame.font.Font(None, CHIP_FONT)


#background color
screen.fill(BG_COLOR)
# call draw function w/n board and draw initial board
#board.draw()

#initalize game state
#FIXME Add game state variables as needed

# modify draw_game_start from tictactoe to be Sudoku focused
def draw_game_start(screen):
  # Initialize title font
  #FIXME Verify fonts/sizes compared to spec
  start_title_font = pygame.font.Font(None, 100)
  subtitle_font = pygame.font.Font(None, 70)
  button_font = pygame.font.Font(None, 50)

  # Color background
  screen.fill(BG_COLOR)

  # Initialize and draw title
  #FIXME Verify title size/font
  title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
  title_rectangle = title_surface.get_rect(
      center=(WIDTH // 2, HEIGHT // 2 - 150))
  screen.blit(title_surface, title_rectangle)

  #initalize and draw subtitle
  #FIXME Verify subtitle size/font
  subtitle_surface = subtitle_font.render("Select Game Mode:", 0, LINE_COLOR)
  subtitle_rectangle = subtitle_surface.get_rect(
      center=(WIDTH // 2, HEIGHT // 2))
  screen.blit(subtitle_surface, subtitle_rectangle)

  # Initialize buttons
  # Initialize text first
  #FIXME Adjust sizes and fonts, as well as line weights, watch video on canvas
  easy_text = button_font.render("EASY", 0, (255, 255, 255))
  medium_text = button_font.render("MEDIUM", 0, (255, 255, 255))
  hard_text = button_font.render("HARD", 0, (255, 255, 255))

  # Initialize button background color and text
  #FIXME NOT STARTED
  easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
  easy_surface.fill(LINE_COLOR)
  easy_surface.blit(easy_text, (10, 10))
  medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
  medium_surface.fill(LINE_COLOR)
  medium_surface.blit(medium_text, (10, 10))
  hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
  hard_surface.fill(LINE_COLOR)
  hard_surface.blit(hard_text, (10, 10))

  # Initialize button rectangle
  #FIXME NOT STARTED
  easy_rectangle = easy_surface.get_rect(
      center=(WIDTH // 2 - 200, HEIGHT // 2 + 150))
  medium_rectangle = medium_surface.get_rect(
      center=(WIDTH // 2, HEIGHT // 2 + 150))
  hard_rectangle = hard_surface.get_rect(
    center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))

  # Draw buttons
  #FIXME NOT STARTED
  screen.blit(easy_surface, easy_rectangle)
  screen.blit(medium_surface, medium_rectangle)
  screen.blit(hard_surface, hard_rectangle)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if easy_rectangle.collidepoint(event.pos):
          # Checks if mouse is on start button
          return  # If the mouse is on the start button, we can return to main
        elif medium_rectangle.collidepoint(event.pos):
          # If the mouse is on the quit button, exit the program
          sys.exit()
        elif hard_rectangle.collidepoint(event.pos):
          # If the mouse is on the quit button, exit the program
          sys.exit()
    pygame.display.update()

draw_game_start(screen)

#initialize event loop
while True:
  for event in pygame.event.get():

    if event.type == pygame.quit():
      pygame.quit()
      sys.exit()
    #listen for mouse click

    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      row = y // SQUARE_SIZE
      col = x // SQUARE_SIZE
      #select a square given row and col index
      #highlight the cell using select function

  pygame.display.update()

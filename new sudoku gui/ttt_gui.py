import pygame, sys #sys --> prevents an pygame.error when window closed
from constants import *
from sudoku import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set width and height of board, changed to 900px,1000px
pygame.display.set_caption('Sudoku') #window screen name

#======================INITIALIZE THE MAIN MENU / RETURN VALUE FOR DIFFICULTY===========================

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
          # Checks if mouse is on start button
          return 30  # If the mouse is on the start button, we can return to main
        elif medium_rectangle.collidepoint(event.pos):
          # If the mouse is on the quit button, exit the program
          return 40
        elif hard_rectangle.collidepoint(event.pos):
          # If the mouse is on the quit button, exit the program
          return 50
    pygame.display.update()

removed = draw_game_start(screen)
#====================INITIALIZE THE GAME STATE HERE (video 3 starts @ min 1:09)=========================
board = initialize_board()    #٩(^ᗜ^ )و ´-
#player = 1 ***Dont think we need this
#chip_type = 'x' #need to figure out how to ask user for number they want
#game_over = False
#winner = 0 #0 mean 'no winner yet', '1'== 'player won', '2' == 'player lost'

chip_type = '1'

#~~~~~Demonstration Purpose Only **Can Delete Later On~~~~~~~~

#Show How To Add Number Chips On the Board
'''
board[0][0] = '1'
board[0][1] = '2'
board[0][2] = '3'
board[0][3] = '4'
board[0][4] = '5'
board[0][5] = '6'
board[0][6] = '7'
board[0][7] = '8'
board[0][8] = '9'

board[0][0] = '1'
board[1][0] = '2'
board[2][0] = '3'
board[3][0] = '4'
board[4][0] = '5'
board[5][0] = '6'
board[6][0] = '7'
board[7][0] = '8'
board[8][0]= '9'
'''
#==================================CHIP CREATION HERE=======================================
#need numbers 1,2,3,4,5,6,7,8,9, and maybe 0???
chip_font = pygame.font.Font(None, CHIP_FONT) #denotes the size of font.

def draw_chips():
  #represents each chip's surface
  chip_1_surf = chip_font.render('1', 0, NUMBER_COLOR)
  chip_2_surf = chip_font.render('2', 0, NUMBER_COLOR)
  chip_3_surf = chip_font.render('3', 0, NUMBER_COLOR)
  chip_4_surf = chip_font.render('4', 0, NUMBER_COLOR)
  chip_5_surf = chip_font.render('5', 0, NUMBER_COLOR)
  chip_6_surf = chip_font.render('6', 0, NUMBER_COLOR)
  chip_7_surf = chip_font.render('7', 0, NUMBER_COLOR)
  chip_8_surf = chip_font.render('8', 0, NUMBER_COLOR)
  chip_9_surf = chip_font.render('9', 0, NUMBER_COLOR)
  #chip_0_surf = chip_font.render('0', 0, NUMBER_COLOR) #dont know if '0' is required

  #represents each chip's rectangle
  #found out that center=(450,450) is the middle of this board
  
  #iterate through the cells using nested for loops
  for row in range(CELL_ROWS): #go through the rows first....
    for col in range(CELL_COLS): #then in each row, we want to look at the col...
      
      if board[row][col] == '1': #seeing if the specific cell is equal to 1
        chip_1_rect = chip_1_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_1_surf, chip_1_rect) #draws numbers on cell/board ---> (surface is first, rect is second)
        
      elif board[row][col] == '2':
        chip_2_rect = chip_2_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_2_surf, chip_2_rect)

      elif board[row][col] == '3':
        chip_3_rect = chip_3_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_3_surf, chip_3_rect)

      elif board[row][col] == '4':
        chip_4_rect = chip_4_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_4_surf, chip_4_rect)

      elif board[row][col] == '5':
        chip_5_rect = chip_5_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_5_surf, chip_5_rect)

      elif board[row][col] == '6':
        chip_6_rect = chip_6_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_6_surf, chip_6_rect)

      elif board[row][col] == '7':
        chip_7_rect = chip_7_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_7_surf, chip_7_rect)

      elif board[row][col] == '8':
        chip_8_rect = chip_8_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_8_surf, chip_8_rect)

      elif board[row][col] == '9':
        chip_9_rect = chip_9_surf.get_rect(center=(col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_9_surf, chip_9_rect)

      '''
      elif board[row][col] == '0':
        chip_0_rect = chip_0_surf.get_rect(center=(col* col* CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(chip_0_surf, chip_0_rect) 
      
      '''

#==================================BOARD CREATION HERE=======================================

def draw_grid():

  #~~~~~~~~~~DRAWING CELL HORIZONTAL LINE HERE~~~~~~~~~~~~~~~~~~~~~~
  for i in range(0, CELL_ROWS): #total cell rows is 9
    pygame.draw.line( 
      screen, #looks at whole screen window
      LINE_COLOR_GRAY,  #line color becomes gray
      (0, i * CELL_SIZE), # Each Big Square is 300 by 300, so each Cell is 100 by 100
      (WIDTH, i * CELL_SIZE),
      LINE_WIDTH_SMALLER #Smaller line thickness for gray lines
  )

  #~~~~~~~~~~DRAWING CELL VERTICAL LINE HERE~~~~~~~~~~~~~~~~~~~~~~
  for i in range(0, CELL_COLS): #total cell cols is 9
    pygame.draw.line(
      screen,
      LINE_COLOR_GRAY,
      (i * CELL_SIZE, 0),
      (i * CELL_SIZE, HEIGHT - 100), #-100 prevents lines from going all the way down
      LINE_WIDTH_SMALLER
    )

  #~~~~~~~~~~DRAWING BOARD HORIZONTAL LINE HERE~~~~~~~~~~~~~~~~~~~~~~
  for i in range(0, BOARD_ROWS + 1): #BOARD_ROWS = 3, so three lines will be drawn
    pygame.draw.line(
      screen, #1st arguement --> the screen(with our full length and height)
      LINE_COLOR_BLACK, #2nd arguement ---> the color you want the lines to be.
      (0, i * SQUARE_SIZE), #3rd argument ---> starting point of line /// SQUARE_SIZE = 300(len&wid of single box)
      (WIDTH, i * SQUARE_SIZE), #4th argument ---> ending point of line
      LINE_WIDTH #5th arguement ---> line thickness
    )
    
  #~~~~~~~~~~DRAWING BOARD VERTIICAL LINE HERE~~~~~~~~~~~~~~~~~~~~~~
  for i in range(0, BOARD_COLS):
    pygame.draw.line(
      screen,
      LINE_COLOR_BLACK,
      (i * SQUARE_SIZE, 0),
      (i * SQUARE_SIZE, HEIGHT-100),  #Substracted 100px from height to get blank bottom space
      LINE_WIDTH
    ) 

#====================Game-In-Progress Window(BOARD Grid) APPEARS HERE!==============================
screen.fill(BG_COLOR_IN_GAME) # Screen represents window screen(predetermined width and height from constants.py)

draw_grid() #makes def draw_grid execute ---> displays our board
draw_chips()


    
#======================================MAIN LOOP=====================================================

while True:
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~EVENT LOOP STARTS HERE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  for event in pygame.event.get():

    #-----------CLOSE WINDOW OPTION HERE (**Not Fully Implemented???**)------------------
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() #sys --> prevents an pygame.error when window closed
      
    #------MOUSECLICK HERE---------------------
    
    #First Click a cellbox
    if event.type == pygame.MOUSEBUTTONDOWN:
      #program is listening for a mouseclick.
      x , y = event.pos
      
      ''' 
      **Delete Later On**
        #prints out x and y coordinates on console 
        #useful to find location/position of a specific click!
      print(x, y)
      
      '''      
      ''' 
      **Delete Later On**
        #prints out row and col indexes on console 
        #useful to find location/position of a specific click!es row_index
        row = y // CELL_SIZE #determine row_index  
        col = x // CELL_SIZE #determines col_index
        print(row, col)
      '''

      row = y // CELL_SIZE #determines row_index
      col = x // CELL_SIZE #determines col_index
      print(row, col)

    #Press a number on the keyboard
    #number will appear on board. K_# doesnt include numberpad, K_KP# is for pressing # on the number pad.
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        board[row][col] = '1'
      elif event.key == pygame.K_2:
        board[row][col] = '2'
      elif event.key == pygame.K_3:
        board[row][col] = '3'
      elif event.key == pygame.K_4:
        board[row][col] = '4'
      elif event.key == pygame.K_5:
        board[row][col] = '5'
      elif event.key == pygame.K_6:
        board[row][col] = '6'
      elif event.key == pygame.K_7:
        board[row][col] = '7'
      elif event.key == pygame.K_8:
        board[row][col] = '8'
      elif event.key == pygame.K_9:
        board[row][col] = '9'
        
      else:
        if event.key == pygame.K_KP1:
          board[row][col] = '1'
        elif event.key == pygame.K_KP2:
          board[row][col] = '2'
        elif event.key == pygame.K_KP3:
          board[row][col] = '3'
        elif event.key == pygame.K_KP4:
          board[row][col] = '4'
        elif event.key == pygame.K_KP5:
          board[row][col] = '5'
        elif event.key == pygame.K_KP6:
          board[row][col] = '6'
        elif event.key == pygame.K_KP7:
          board[row][col] = '7'
        elif event.key == pygame.K_KP8:
          board[row][col] = '8'
        elif event.key ==  pygame.K_KP9:
          board[row][col] = '9'

    #prints number using draw_chips()
    #error: number can be paced on top of each other if the same cell box is selected
    #problem: code didnt work when I did an 'or statement', such as == (pygame.K_KP1) or (pygame.K_1)
    draw_chips() 
  
  pygame.display.update() # Needs to be at the end of the event For Loop! Updates the Window Screen at the end of loop.     
pass

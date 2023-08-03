"""
This class represents a single cell object within a Sudoku board object.

Authors: Samson Carter, Chance Nahuway, Dylan Dixon, Diamond Nicholas
Project 4, Group 1
UF COP 3502C in Summer 2023.
"""


from constants import *
import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.is_selected = False
        if self.value == 0:
            self.is_editable = True
        else:
            self.is_editable = False

    def set_cell_value(self, value):
        if self.is_editable:
            self.value = value

    def set_sketched_value(self, sketched_value):
        if self.is_editable:
            self.sketched_value = sketched_value

    def draw(self):
        num_font = pygame.font.Font(None, NUMBER_FONT)
        cell_1_surf = num_font.render('1', 0, NUMBER_COLOR)
        cell_2_surf = num_font.render('2', 0, NUMBER_COLOR)
        cell_3_surf = num_font.render('3', 0, NUMBER_COLOR)
        cell_4_surf = num_font.render('4', 0, NUMBER_COLOR)
        cell_5_surf = num_font.render('5', 0, NUMBER_COLOR)
        cell_6_surf = num_font.render('6', 0, NUMBER_COLOR)
        cell_7_surf = num_font.render('7', 0, NUMBER_COLOR)
        cell_8_surf = num_font.render('8', 0, NUMBER_COLOR)
        cell_9_surf = num_font.render('9', 0, NUMBER_COLOR)
        cell_0_surf = num_font.render('', 0, NUMBER_COLOR)

        if self.value == 1:
            cell_1_rect = cell_1_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_1_surf, cell_1_rect)
        elif self.value == 2:
            cell_2_rect = cell_2_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_2_surf, cell_2_rect)
        elif self.value == 3:
            cell_3_rect = cell_3_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_3_surf, cell_3_rect)
        elif self.value == 4:
            cell_4_rect = cell_4_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_4_surf, cell_4_rect)
        elif self.value == 5:
            cell_5_rect = cell_5_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_5_surf, cell_5_rect)
        elif self.value == 6:
            cell_6_rect = cell_6_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_6_surf, cell_6_rect)
        elif self.value == 7:
            cell_7_rect = cell_7_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_7_surf, cell_7_rect)
        elif self.value == 8:
            cell_8_rect = cell_8_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_8_surf, cell_8_rect)
        elif self.value == 9:
            cell_9_rect = cell_9_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_9_surf, cell_9_rect)
        elif self.value == 0:
            cell_0_rect = cell_0_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(cell_0_surf, cell_0_rect)

        sketched_num_font = pygame.font.Font(None, SKETCHED_NUMBER_FONT)
        sketched_cell_1_surf = sketched_num_font.render('1', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_2_surf = sketched_num_font.render('2', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_3_surf = sketched_num_font.render('3', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_4_surf = sketched_num_font.render('4', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_5_surf = sketched_num_font.render('5', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_6_surf = sketched_num_font.render('6', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_7_surf = sketched_num_font.render('7', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_8_surf = sketched_num_font.render('8', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_9_surf = sketched_num_font.render('9', 0, SKETCHED_NUMBER_COLOR)
        sketched_cell_0_surf = sketched_num_font.render('', 0, SKETCHED_NUMBER_COLOR)

        if self.sketched_value == 1:
            sketched_cell_1_rect = sketched_cell_1_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_1_surf, sketched_cell_1_rect)
        elif self.sketched_value == 2:
            sketched_cell_2_rect = sketched_cell_2_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_2_surf, sketched_cell_2_rect)
        elif self.sketched_value == 3:
            sketched_cell_3_rect = sketched_cell_3_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_3_surf, sketched_cell_3_rect)
        elif self.sketched_value == 4:
            sketched_cell_4_rect = sketched_cell_4_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_4_surf, sketched_cell_4_rect)
        elif self.sketched_value == 5:
            sketched_cell_5_rect = sketched_cell_5_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_5_surf, sketched_cell_5_rect)
        elif self.sketched_value == 6:
            sketched_cell_6_rect = sketched_cell_6_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_6_surf, sketched_cell_6_rect)
        elif self.sketched_value == 7:
            sketched_cell_7_rect = sketched_cell_7_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_7_surf, sketched_cell_7_rect)
        elif self.sketched_value == 8:
            sketched_cell_8_rect = sketched_cell_8_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_8_surf, sketched_cell_8_rect)
        elif self.sketched_value == 9:
            sketched_cell_9_rect = sketched_cell_9_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_9_surf, sketched_cell_9_rect)
        elif self.sketched_value == 0:
            sketched_cell_0_rect = sketched_cell_0_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_0_surf, sketched_cell_0_rect)

    def erase_sketched_number(self):
        sketched_num_font = pygame.font.Font(None, SKETCHED_NUMBER_FONT)
        sketched_cell_1_surf = sketched_num_font.render('1', 0, BG_COLOR_IN_GAME)
        sketched_cell_2_surf = sketched_num_font.render('2', 0, BG_COLOR_IN_GAME)
        sketched_cell_3_surf = sketched_num_font.render('3', 0, BG_COLOR_IN_GAME)
        sketched_cell_4_surf = sketched_num_font.render('4', 0, BG_COLOR_IN_GAME)
        sketched_cell_5_surf = sketched_num_font.render('5', 0, BG_COLOR_IN_GAME)
        sketched_cell_6_surf = sketched_num_font.render('6', 0, BG_COLOR_IN_GAME)
        sketched_cell_7_surf = sketched_num_font.render('7', 0, BG_COLOR_IN_GAME)
        sketched_cell_8_surf = sketched_num_font.render('8', 0, BG_COLOR_IN_GAME)
        sketched_cell_9_surf = sketched_num_font.render('9', 0, BG_COLOR_IN_GAME)
        sketched_cell_0_surf = sketched_num_font.render('', 0, BG_COLOR_IN_GAME)

        if self.sketched_value == 1:
            sketched_cell_1_rect = sketched_cell_1_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_1_surf, sketched_cell_1_rect)
        elif self.sketched_value == 2:
            sketched_cell_2_rect = sketched_cell_2_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_2_surf, sketched_cell_2_rect)
        elif self.sketched_value == 3:
            sketched_cell_3_rect = sketched_cell_3_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_3_surf, sketched_cell_3_rect)
        elif self.sketched_value == 4:
            sketched_cell_4_rect = sketched_cell_4_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_4_surf, sketched_cell_4_rect)
        elif self.sketched_value == 5:
            sketched_cell_5_rect = sketched_cell_5_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_5_surf, sketched_cell_5_rect)
        elif self.sketched_value == 6:
            sketched_cell_6_rect = sketched_cell_6_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_6_surf, sketched_cell_6_rect)
        elif self.sketched_value == 7:
            sketched_cell_7_rect = sketched_cell_7_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_7_surf, sketched_cell_7_rect)
        elif self.sketched_value == 8:
            sketched_cell_8_rect = sketched_cell_8_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_8_surf, sketched_cell_8_rect)
        elif self.sketched_value == 9:
            sketched_cell_9_rect = sketched_cell_9_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_9_surf, sketched_cell_9_rect)
        elif self.sketched_value == 0:
            sketched_cell_0_rect = sketched_cell_0_surf.get_rect(
                center=(self.row * SQUARE_SIZE + SQUARE_SIZE // 4.5, self.col * SQUARE_SIZE + SQUARE_SIZE // 4))
            self.screen.blit(sketched_cell_0_surf, sketched_cell_0_rect)

        '''if self.is_selected is True:
            for i in range(self.row, self.row + 2):
                pygame.draw.line(self.screen, SELECTED_COLOR, (self.col * SQUARE_SIZE, i * SQUARE_SIZE),
                                 ((self.col + 1) * SQUARE_SIZE, i * SQUARE_SIZE), LINE_WIDTH)
            for i in range(self.col, self.col + 2):
                pygame.draw.line(self.screen, SELECTED_COLOR, (i * SQUARE_SIZE, self.row * SQUARE_SIZE),
                                 (i * SQUARE_SIZE, (self.row + 1) * SQUARE_SIZE), LINE_WIDTH)'''

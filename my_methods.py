class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells

    def valid_in_col(self, col, num):
        col_list = []
        for cell in range(9):
            col_list.append(self.board[cell][col])
        if num in col_list:
            return False
        else:
            return True


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        num_font = pygame.font.Font(None, NUM_FONT)
        cell_1_surf = num_font.render('1', 0, NUM_COLOR)
        cell_2_surf = num_font.render('2', 0, NUM_COLOR)
        cell_3_surf = num_font.render('3', 0, NUM_COLOR)
        cell_4_surf = num_font.render('4', 0, NUM_COLOR)
        cell_5_surf = num_font.render('5', 0, NUM_COLOR)
        cell_6_surf = num_font.render('6', 0, NUM_COLOR)
        cell_7_surf = num_font.render('7', 0, NUM_COLOR)
        cell_8_surf = num_font.render('8', 0, NUM_COLOR)
        cell_9_surf = num_font.render('9', 0, NUM_COLOR)
        cell_blank_surf = num_font.render('', 0, NUM_COLOR)

        if self.value == '1':
            cell_1_rect = cell_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_1_surf, cell_1_rect)
        elif self.value == '2':
            cell_2_rect = cell_2_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_2_surf, cell_2_rect)
        elif self.value == '3':
            cell_3_rect = cell_3_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_3_surf, cell_3_rect)
        elif self.value == '4':
            cell_4_rect = cell_4_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_4_surf, cell_4_rect)
        elif self.value == '5':
            cell_5_rect = cell_5_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_5_surf, cell_5_rect)
        elif self.value == '6':
            cell_6_rect = cell_6_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_6_surf, cell_6_rect)
        elif self.value == '7':
            cell_7_rect = cell_7_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_7_surf, cell_7_rect)
        elif self.value == '8':
            cell_8_rect = cell_8_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_8_surf, cell_8_rect)
        elif self.value == '9':
            cell_9_rect = cell_9_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_9_surf, cell_9_rect)
        else:
            cell_blank_rect = cell_blank_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(cell_blank_surf, cell_blank_rect)
import random
import pygame

pygame.init()

# initial setup
width = 400
height = 500
screen = pygame.display.set_mode([height, width])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)


# 2048 colour library
colours = {0: (204, 192, 179),
           2: (238, 228, 218),
           4: (237, 224, 200),
           8: (242, 177, 121),
           16: (245, 149, 99),
           32: (246, 124, 95),
           64: (246, 94, 59),
           128: (237, 204, 97),
           256: (237, 204, 114),
           512: (237, 200, 80),
           1024: (237, 197, 63),
           2048: (237, 194, 46),
           'light-text': (249, 246, 242),
           'dark text': (119, 110, 101),
           'other': (0, 0, 0),
           'bg': (107, 173, 160)}


board_val = [[0 for _ in range(4) for _ in range(4)]]


def draw_board():
    pygame.draw.rect(screen, colours['bg'], [0, 0, 400, 400], 0, 10)
    pass

# draw pieces for the board


def draw_pieces(board):

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_val)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()

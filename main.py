import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 36
SCORE_FONT_SIZE = 24
SCORE_OFFSET = 10
FPS = 60

# Directional constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Colors for each tile value (powers of 2)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Function to initialize the game board
def initialize_board():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Function to add a new tile to the board
def add_new_tile(board):
   pass
# Function to draw the game board
def draw_board(screen, board):
    screen.fill(BACKGROUND_COLOR)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = board[i][j]
            color = TILE_COLORS.get(value, TILE_COLORS[0])
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                draw_text(screen, str(value), (j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))

# Function to draw text on the screen
def draw_text(screen, text, position):
    pass

# Function to draw the score
def draw_score(screen, score):
   pass

# Function to move the tiles in a given direction
def move_tiles(board, direction):
   pass


# Function to check if the game is over
def is_game_over(board):
   pass
# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Game")
    clock = pygame.time.Clock()

    board = initialize_board()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moved = move_tiles(board, UP)
                elif event.key == pygame.K_DOWN:
                    moved = move_tiles(board, DOWN)
                elif event.key == pygame.K_LEFT:
                    moved = move_tiles(board, LEFT)
                elif event.key == pygame.K_RIGHT:
                    moved = move_tiles(board, RIGHT)

                if moved:
                    add_new_tile(board)

        draw_board(screen, board)
        draw_score(screen, score)
        pygame.display.flip()

        if is_game_over(board):
            print("Game Over! Your score: {}".format(score))
            pygame.quit()
            quit()

        clock.tick(FPS)

if __name__ == "__main__":
    main()

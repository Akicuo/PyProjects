import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = HEIGHT // ROWS

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Set up the board
board = []
for row in range(ROWS):
    board_row = []
    for col in range(COLS):
        if (row + col) % 2 == 0:
            board_row.append(WHITE)
        else:
            board_row.append(BLACK)
    board.append(board_row)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the board
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, board[row][col], (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()
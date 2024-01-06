import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col, n):
    if col == n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_queens(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def draw_chessboard(screen, n):
    width = height = 600
    cell_size = width // n

    screen.fill(WHITE)

    for i in range(n + 1):
        pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 2)
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 2)

    pygame.display.flip()

def draw_queens(screen, board):
    cell_size = screen.get_width() // len(board)

    queen_image = pygame.image.load("queen.png")
    queen_image = pygame.transform.scale(queen_image, (cell_size, cell_size))

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                screen.blit(queen_image, (col * cell_size, row * cell_size))

    pygame.display.flip()

def main():
    n = 10
    board = [[0 for _ in range(n)] for _ in range(n)]

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Chessboard")

    draw_chessboard(screen, n)

    if solve_queens(board, 0, n):
        draw_queens(screen, board)
    else:
        print("چینش ممکن نیست.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

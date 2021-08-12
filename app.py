import pygame as pg
import sys
from play.colors import Color


def is_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign + " wins"
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign + " wins"
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign + " wins"
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign + " wins"
    if zeroes == 0:
        return "Piece"
    return False


pg.init()
size_block = 100
margin = 8
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pg.display.set_mode(size_window)
pg.display.set_caption("Tic Tac Toe")

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = "x"
                else:
                    mas[row][col] = "o"
                query += 1
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(Color.BLACK)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == "x":
                    color = Color.GREEN
                elif mas[row][col] == "o":
                    color = Color.BLUE
                else:
                    color = Color.LIGHT_GRAY
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pg.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == Color.GREEN:
                    pg.draw.line(screen, Color.WHITE, (x + 10, y + 10), (x + size_block - 10, y + size_block - 10), 8)
                    pg.draw.line(screen, Color.WHITE, (x + size_block - 10, y + 10), (x + 10, y + size_block - 10), 8)
                elif color == Color.BLUE:
                    pg.draw.circle(screen, Color.WHITE, (x + size_block // 2, y + size_block // 2), size_block // 2 - 8,
                                   8)

    if (query - 1) % 2 == 0:  # x
        game_over = is_win(mas, "x")
    else:
        game_over = is_win(mas, "o")

    if game_over:
        screen.fill(Color.BLACK)
        font = pg.font.SysFont("stxingkai", 80)
        text1 = font.render(game_over, True, Color.WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2  # center of the screen
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pg.display.update()

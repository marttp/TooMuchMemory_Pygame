import pygame, sys, random, grid_library
from pygame.locals import *


def main():
    clicked = 0
    click = 0
    dual = 0

    class Square():
        def __init__(self, rect, color):
            self.rect = rect
            self.color = color
            self.match = False
            self.viewable_trigger = False

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Too Much Memory")
    testrun = False
    # GRIDSIZE = 16
    #
    # if GRIDSIZE == 4 or GRIDSIZE == 16:
    #     pass
    # else:
    #     print("Grid must be size 4 or 16.")
    #     print("Exiting program.  Fix the code.")
    #     exit()

    # SCREENWIDTH = 720
    SCREENWIDTH = 800
    SCREENHEIGHT = 800
    # SCREENHEIGHT = 1280
    SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

    max_color_occurences = 2

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    grid = grid_library.Grid(SCREENSIZE)

    number_colors = len(grid.color_name_list)

    windowSurface = pygame.display.set_mode(SCREENSIZE)

    color_occurence_dict = {}
    for color in grid.color_name_list:
        color_occurence_dict.update({color: 0})

    squares_list = []  # create empty list of Square objects

    for y in range(0, grid.screenheight, grid.square_height):
        for x in range(0, 600, grid.square_width):
            rect = pygame.Rect(x, y, grid.square_width, grid.square_height)

            color_key = random.choice(grid.color_name_list)
            if color_occurence_dict[color_key] < max_color_occurences:
                color_occurence_dict[color_key] += 1

            else:
                color_key = random.choice(grid.color_name_list)

                while color_occurence_dict[color_key] >= max_color_occurences:
                    color_key = random.choice(grid.color_name_list)
                color_occurence_dict[color_key] += 1

            color = color_key
            square = Square(rect, color)
            squares_list.append(square)

    count = 0

    clock = pygame.time.Clock()
    FPS = 50

    while True:
        for event in pygame.event.get():
            #print(event)
            x, y = pygame.mouse.get_pos()

            if event.type == QUIT: #or (x > 650 and x < 755 and y > 650 and y < 700):
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if x < 600:
                    if count < 2:
                        count += 1
                    else:
                        count = 0

                    if click < 10:
                        if pygame.font:
                            font = pygame.font.Font(None, 80)
                            text1 = font.render(str(click), 0, (0, 0, 0))
                            textpos1 = text1.get_rect(x=695, y=230)
                            windowSurface.blit(text1, textpos1)
                        else:
                            print("not font")
                    elif click < 100:
                        if pygame.font:
                            font = pygame.font.Font(None, 80)
                            text1 = font.render(str(click), 0, (0, 0, 0))
                            textpos1 = text1.get_rect(x=675, y=230)
                            windowSurface.blit(text1, textpos1)
                        else:
                            print("not font")
                    else:
                        if pygame.font:
                            font = pygame.font.Font(None, 80)
                            text1 = font.render(str(click), 0, (0, 0, 0))
                            textpos1 = text1.get_rect(x=655, y=230)
                            windowSurface.blit(text1, textpos1)
                        else:
                            print("not font")

                    clicked += 1
                    if clicked % 3 == 0:
                        click += 1

                    print(click)

                    for square in squares_list:
                        if square.rect.collidepoint(x, y):
                            square.viewable_trigger = True
                elif 650 < x < 755 and 650 < y < 700:
                    pygame.quit()
                    sys.exit()
                elif 650 < x < 755 and 580 < y < 630:
                    pygame.quit()
                    return

        for square_object in squares_list:
            if not square_object.match:
                pygame.draw.rect(windowSurface, BLACK, square_object.rect)

        if testrun:
            for square in squares_list:
                pygame.draw.rect(windowSurface, square.color, square.rect)

        if count == 1 or count == 2:
            for square in squares_list:
                if square.viewable_trigger:
                    pygame.draw.rect(windowSurface, square.color, square.rect)
                    if count == 1:
                        index_first_viewable_square = squares_list.index(square)

                    elif count == 2:

                        index_current_viewable = squares_list.index(square)

                        if index_current_viewable != index_first_viewable_square:
                            index_second_viewable = index_current_viewable
                            first_color = squares_list[index_first_viewable_square].color
                            second_color = squares_list[index_second_viewable].color

                            if first_color == second_color:
                                squares_list[index_first_viewable_square].match = True
                                squares_list[index_second_viewable].match = True


        else:
            count = 0
            for square in squares_list:
                square.viewable_trigger = False

        if pygame.font:
            font = pygame.font.Font(None, 50)
            text = font.render("Clicked", 0, (255, 255, 255))
            textpos = text.get_rect(x=645, y=120)
            windowSurface.blit(text, textpos)

            if click < 10:
                if pygame.font:
                    font = pygame.font.Font(None, 80)
                    text1 = font.render(str(click), 0, (255, 255, 255))
                    textpos1 = text1.get_rect(x=695, y=230)
                    windowSurface.blit(text1, textpos1)
            elif click < 100:
                if pygame.font:
                    font = pygame.font.Font(None, 80)
                    text1 = font.render(str(click), 0, (255, 255, 255))
                    textpos1 = text1.get_rect(x=675, y=230)
                    windowSurface.blit(text1, textpos1)
            else:
                if pygame.font:
                    font = pygame.font.Font(None, 80)
                    text1 = font.render(str(click), 0, (255, 255, 255))
                    textpos1 = text1.get_rect(x=655, y=230)
                    windowSurface.blit(text1, textpos1)
        else:
            print("not font")

        pygame.draw.rect(windowSurface, (0, 220, 0), (655, 580, 100, 50))
        font3 = pygame.font.Font(None, 35)
        text3 = font3.render("Reset", 0, (255, 255, 255))
        textpos3 = text3.get_rect(x=675, y=595)
        windowSurface.blit(text3, textpos3)

        pygame.draw.rect(windowSurface, (255, 0, 0), (655, 650, 100, 50))
        font2 = pygame.font.Font(None, 35)
        text2 = font2.render("Exit", 0, (255, 255, 255))
        textpos2 = text2.get_rect(x=680, y=665)
        windowSurface.blit(text2, textpos2)

        grid.draw_lines(windowSurface)
        clock.tick(FPS)
        pygame.display.update()


while True:
    main()

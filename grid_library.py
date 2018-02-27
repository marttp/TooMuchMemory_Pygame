import pygame, random


class Grid():
    def __init__(self, screensize):
        # self.size = grid_size
        self.screensize = screensize
        self.screenwidth = screensize[0]
        self.screenheight = screensize[1]

        # self.num_columns = self.num_rows = int(math.sqrt(self.size))

        # self.square_width = int(self.screenwidth / self.num_columns)
        # self.square_height = int(self.screenheight / self.num_rows)
        self.square_width = 100
        self.square_height = 100

        self.load_colors()

    def load_colors(self):

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.color_name_list = list()
        for i in range(24):
            self.color_name_list.append(
                tuple((random.randrange(0, 255, 16), random.randrange(0, 255, 16), random.randrange(0, 255, 16))))

    def draw_lines(self, windowSurface,click):
        # if pygame.font:
        #     font = pygame.font.Font(None, 50)
        #     text = font.render("Clicked", 1, (255, 255, 255))
        #     textpos = text.get_rect(x=645, y=120)
        #     text1 = font.render(str(click), 1, (255, 255, 255))
        #     textpos1 = text1.get_rect(x=695, y=230)
        #     windowSurface.blit(text, textpos)
        #     windowSurface.blit(text1, textpos1)
        # else:
        #     print("not font")

        for x in range(0, 700, self.square_width):
            pygame.draw.line(windowSurface, self.WHITE, (x, 0), (x, self.screenheight), 3)
        for y in range(0, self.screenheight, self.square_height):
            pygame.draw.line(windowSurface, self.WHITE, (0, y), (600, y), 3)

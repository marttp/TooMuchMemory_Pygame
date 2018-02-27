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

    def draw_lines(self, windowSurface):
        for x in range(0, 700, self.square_width):
            pygame.draw.line(windowSurface, self.WHITE, (x, 0), (x, self.screenheight), 3)
        for y in range(0, self.screenheight, self.square_height):
            pygame.draw.line(windowSurface, self.WHITE, (0, y), (600, y), 3)

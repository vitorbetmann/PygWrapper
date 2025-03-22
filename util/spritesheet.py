import pygame
import sys
from pygame.surface import Surface


class SpriteSheet:
    """A class to manage sprite sheets.

    Args:
        filename (image | str): The Image object or the file location of the sprite sheet.
        *args (tuple | int): Requires the dimensions of the rect that will
            "cut" the sprites off the original image. Additional arguments are
            the starting x and y positions of the top left corner of the rect
            (if x is given, y is expected, otherwise, they both default to 0).
        limit (int): The maximum number of sprite sheets to load. Limit must be stated
            as a keyword argument (default is None).


    Attributes:
        sprite_sheet #read only

    Methods:
        append_sprite(rect_topleft, rect_size)

    Raises:
        pygame.error

    Typical usage example:

      ss = SpriteSheet(filename='sprite_sheet.png', (10, 10))
      #The constructor cuts up the image in 10x10 rects and stores the Surfaces in sprite_sheet

      ss = SpriteSheet(filename='sprite_sheet.png', (10, 10))
      #Same as above

      ss = SpriteSheet(filename='sprite_sheet.png', (10, 10), (150, 200))
      #The constructor cuts up the image in 10x10 rects with starting position (150, 200)
        for the topleft rectangle attribute, and the Surfaces are stored in sprite_sheet

      ss = SpriteSheet(filename='sprite_sheet.png', 10, 10, 150, 200)
      #Same as above

      ss = SpriteSheet(filename='sprite_sheet.png', (10, 10), 150, 200)
      ss = SpriteSheet(filename='sprite_sheet.png', '10', '10', '150', '200')
      ss = SpriteSheet(filename='sprite_sheet.png', 10, 150, 200)
      #Raises pygame.error
    """

    def __init__(self, image, *args, limit=None):
        if len(args) == 1 and isinstance(args[0], tuple):
            rect_width = args[0][0]
            rect_height = args[0][1]
            self.start_x = 0
            self.start_y = 0
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            rect_width = args[0]
            rect_height = args[1]
            self.start_x = 0
            self.start_y = 0
        elif (
            len(args) == 2 and isinstance(args[0], tuple) and isinstance(args[1], tuple)
        ):
            rect_width = args[0][0]
            rect_height = args[0][1]
            self.start_x = args[1][0]
            self.start_y = args[1][1]
        elif len(args) == 4:
            for arg in args:
                if not isinstance(arg, int):
                    raise pygame.error("Invalid argument type. Must be of type int.")

            rect_width = args[0]
            rect_height = args[1]
            self.start_x = args[2]
            self.start_y = args[3]
        else:
            raise pygame.error(
                "Invalid number of arguments passed or arguments are of invalid type."
            )

        if isinstance(image, Surface):
            self.image = image
        elif isinstance(image, str):
            try:
                self.image = pygame.image.load(image).convert_alpha()
            except FileNotFoundError:
                raise pygame.error("File not found.")

        self._sprite_sheet = []

        self.rect = pygame.Rect(0, 0, rect_width, rect_height)
        if self.rect:
            if limit:
                self.limit = limit
            else:
                x_steps = int(self.image.get_width() / self.rect.width)
                y_steps = int(self.image.get_height() / self.rect.height)
                self.limit = x_steps * y_steps

            for i in range(self.start_y, self.image.height, self.rect.height):
                for j in range(self.start_x, self.image.width, self.rect.width):
                    if len(self._sprite_sheet) < self.limit:
                        self.append_sprite((j, i), self.rect.size)

    @property
    def sprite_sheet(self):
        return self._sprite_sheet

    def append_sprite(self, rect_topleft, rect_size):
        temp_rect = pygame.Rect(rect_topleft, rect_size)
        temp_surface = pygame.Surface(temp_rect.size)
        temp_surface.blit(self.image, area=temp_rect)
        self._sprite_sheet.append(temp_surface)

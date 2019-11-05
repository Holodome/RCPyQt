import numpy

WHITE = 0x1
YELLOW = 0x2
GREEN = 0x3
BLUE = 0x4
RED = 0x5
ORANGE = 0x6


class Block:
    def __init__(self, x, y, z):
        # WHITE - YELLOW    TOP - BOTTOM
        # GREEN - BLUE      LEFT - RIGHT
        # ORANGE - RED      BACK - FRONT
        self.position = numpy.array([x, y, z], numpy.uint8)
        self.facesColors = numpy.zeros(6, numpy.uint8)

        self.numberOfColors = 0

    def copy(self):
        block = Block.__new__(Block)
        block.position = self.position.copy()
        block.facesColors = self.facesColors.copy()
        block.numberOfColors = self.numberOfColors
        return block

    def set_faces_colors(self, size):
        # BOTTOM TOP LEFT RIGHT BACK FRONT
        if self.position[1] == 0:
            self.facesColors[0] = YELLOW
            self.numberOfColors += 1
        if self.position[1] == size - 1:
            self.facesColors[1] = WHITE
            self.numberOfColors += 1
        if self.position[0] == 0:
            self.facesColors[2] = GREEN
            self.numberOfColors += 1
        if self.position[0] == size - 1:
            self.facesColors[3] = BLUE
            self.numberOfColors += 1
        if self.position[2] == 0:
            self.facesColors[4] = ORANGE
            self.numberOfColors += 1
        if self.position[2] == size - 1:
            self.facesColors[5] = RED
            self.numberOfColors += 1

    def rotate(self, axis: int, clockwise: bool):
        if clockwise:
            self.rotate(axis, False)
            self.rotate(axis, False)
            self.rotate(axis, False)
            return

        new_colors = self.facesColors.copy()

        if axis == 0:
            new_colors[0] = self.facesColors[5]
            new_colors[1] = self.facesColors[4]
            new_colors[4] = self.facesColors[0]
            new_colors[5] = self.facesColors[1]
        elif axis == 1:
            new_colors[2] = self.facesColors[4]
            new_colors[3] = self.facesColors[5]
            new_colors[4] = self.facesColors[3]
            new_colors[5] = self.facesColors[2]
        elif axis == 2:
            new_colors[2] = self.facesColors[1]
            new_colors[3] = self.facesColors[0]
            new_colors[0] = self.facesColors[2]
            new_colors[1] = self.facesColors[3]
        self.facesColors = new_colors

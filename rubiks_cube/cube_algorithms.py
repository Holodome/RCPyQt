import random
from typing import List, Tuple

from .rubiks_cube import RubiksCube


class CubeAlgorithms:
    def __init__(self):
        self.turning: bool = False  # Происходит какое-то действие
        self.scrambleTimesLeft: int = 0

        self.turns: List[Tuple[int, int, bool]] = []
        # Флаги, которые показывают начало алгоритма
        self.makeCheckered = False
        self.makeCubeInCube = False

    # Обновление действий над кубиком
    def update(self, cube: RubiksCube):
        if cube.turning or cube.turningWholeCube:
            return

        if self.scrambleTimesLeft > 0:
            self.rotate_random(cube)
            return

        if self.makeCheckered:
            self.makeCheckered = False
            self.do_checkered(cube)

        if self.makeCubeInCube:
            self.makeCubeInCube = False
            self.do_cube_in_cube(cube)

        if len(self.turns) != 0:
            cube.turn_cube(*self.turns.pop(0))

    def rotate_random(self, cube: RubiksCube):
        self.scrambleTimesLeft -= 1
        if self.scrambleTimesLeft == 0:
            self.turning = False

        ind = random.randrange(cube.size)
        axis = random.randrange(3)
        clockwise = random.randrange(2)
        cube.turn_cube(ind, axis, clockwise)

    def do_checkered(self, cube):
        for a in range(3):
            for ind in filter(lambda n: n % 2 == 0, range(cube.size)):
                self.turns.append((ind, a, True))
                self.turns.append((ind, a, True))

    def do_cube_in_cube(self, cube):
        # F L F U' R U F F L L U' L' B D' B' L L U
        a = cube.size - 1
        basic_outer = [
            (a, 2, 1),  # F
            (0, 0, 0),  # L
            (a, 2, 1),  # F
            (a, 1, 0),  # U'
            (a, 0, 1),  # R
            (a, 1, 1),  # U
            (a, 2, 1),  # F
            (a, 2, 1),  # F
            (0, 0, 0),  # L
            (0, 0, 0),  # L
            (a, 1, 0),  # U'
            (0, 0, 1),  # L'
            (0, 2, 0),  # B
            (0, 1, 1),  # D'
            (0, 2, 1),  # B'
            (0, 0, 0),  # L
            (0, 0, 0),  # L
            (a, 1, 1),  # U
        ]
        # B2
        # R' D R D' R' D R U
        # R' D' R D R' D' R U'
        # B2
        basic_inner = [
            (0, 2, 0),  # B
            (0, 2, 0),  # B

            (a, 0, 0),  # R'
            (0, 1, 0),  # D
            (a, 0, 1),  # R
            (0, 1, 1),  # D'
            (a, 0, 0),  # R'
            (0, 1, 0),  # D
            (a, 0, 1),  # R
            (a, 1, 1),  # U

            (a, 0, 0),  # R'
            (0, 1, 1),  # D'
            (a, 0, 1),  # R
            (0, 1, 0),  # D
            (a, 0, 0),  # R'
            (0, 1, 1),  # D'
            (a, 0, 1),  # R
            (a, 1, 0),  # U'

            (0, 2, 0),  # B
            (0, 2, 0),  # B
        ]

        for i in range(cube.size // 2):  # Большие кубы
            for el in basic_outer:
                for j in range(i + 1):
                    new = (abs(el[0] - j), el[1], el[2])
                    self.turns.append(new)
        for i in range((cube.size - 1) // 2 - 1, -1, -1):  # Меньшие кубы
            for el in basic_inner:
                for j in range(i + 1):
                    new = (abs(el[0] - j), el[1], el[2])
                    self.turns.append(new)

    def set_scramble(self, count):
        self.turning = True
        self.scrambleTimesLeft = count

    def reset(self):
        self.turning = False
        self.scrambleTimesLeft = 0
        self.makeCheckered = False
        self.makeCubeInCube = False

        self.turns.clear()

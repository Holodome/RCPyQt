"""
Всопомогательный статический класс для сохранения и загрузки кубиков
"""
import csv

from .rubiks_cube import RubiksCube


class CubeState:
    @staticmethod
    def save(cube: RubiksCube, filepath: str) -> bool:
        if cube.turning:
            cube.finalise_turn(cube.rotationIndex, cube.rotationAxis, cube.turningClockwise)

        with open(filepath, "w") as out:
            size = cube.size
            writer = csv.writer(out, delimiter=",")
            writer.writerow([size])
            for row in cube.blocks:
                for col in row:
                    for block in col:
                        writer.writerow(block.facesColors)
        return True

    @staticmethod
    def load(filepath: str) -> RubiksCube:
        def cube_iter(c):
            for row in c.blocks:
                for col in row:
                    yield from col

        with open(filepath) as f:
            reader = csv.reader(f, delimiter=",")

            try:
                cube = None
                it = None
                for line in filter(lambda e: e, reader):
                    if cube is None:
                        if len(line) != 1:
                            return None
                        cube = RubiksCube(int(line[0]))
                        it = cube_iter(cube)
                    else:
                        next(it).facesColors = list(map(int, line))
            except Exception:
                print("Incorrect format!")
                return None

        return cube

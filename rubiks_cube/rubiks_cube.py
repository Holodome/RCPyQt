from typing import List

import numpy as np
import pyrr as pr

from .block import Block

ROTATION_SPEED = 400


class RubiksCube:
    def __init__(self, size):
        self.size = size
        self.offset = np.array([-(size - 1), -(size - 1), -(size - 1)], dtype=np.float32)

        self.blockSize: pr.Vector3 = pr.Vector3([3 / size, 3 / size, 3 / size])

        self.blocks = []
        for x in range(size):
            row = []
            for y in range(size):
                col = []
                for z in range(size):
                    block = Block(x, y, z)
                    block.set_faces_colors(size)
                    col.append(block)
                row.append(col)
            self.blocks.append(row)

        self.rotatingBlocks: List[Block] = []
        self.cycleLists: List[List[Block]] = []

        self.turningClockwise: bool = True
        self.turningWholeCube: bool = False
        self.turning: bool = False

        self.rotationAngle: int = 0
        self.rotationIndex: int = 0
        self.rotationAxis: int = 0

    def update(self, dt):
        if self.turning:
            if self.rotationAngle < 90.0:
                if self.rotationAngle < 22.5:
                    self.rotationAngle += 2 * ROTATION_SPEED / (self.rotationAngle / -22.5 + 2) * dt
                elif self.rotationAngle > 77.5:
                    self.rotationAngle += 2 * ROTATION_SPEED / ((self.rotationAngle - 77.5) / 90 + 1) * dt
                else:
                    self.rotationAngle += 2 * ROTATION_SPEED * dt

            else:
                self.rotationAngle = 0
                if self.turningWholeCube:
                    self.finish_turning_whole_cube(self.rotationAxis, self.turningClockwise)
                else:
                    self.finalise_turn(self.rotationIndex, self.rotationAxis, self.turningClockwise)

    def turn_whole_cube(self, axis: int, clockwise: bool):
        if self.turning:
            self.rotationAngle = 0
            self.finalise_turn(self.rotationIndex, self.rotationAxis, self.turningClockwise)

        self.turning = True
        self.turningWholeCube = True
        self.turningClockwise = clockwise
        self.rotationAxis = axis

    def turn_cube(self, index, axis, turn_clockwise):
        if self.turning:
            self.rotationAngle = 0
            self.finalise_turn(self.rotationIndex, self.rotationAxis, self.turningClockwise)

        self.turning = True
        self.turningClockwise = turn_clockwise
        self.cycleLists = self._get_all_blocks_to_rotate(index, axis)
        self.rotatingBlocks = []
        for i in self.cycleLists:
            self.rotatingBlocks.extend(i)
        self.rotationAxis = axis
        self.rotationIndex = index

    def finalise_turn(self, index: int, axis: int, turn_clockwise: bool):
        self.turning = False
        for block in self.rotatingBlocks:
            block.rotate(axis, turn_clockwise)

        for j, temp in enumerate(self.cycleLists):
            for i in range(self.size - 1 - j * 2):
                if not turn_clockwise:
                    temp.insert(0, temp.pop())
                else:
                    temp.append(temp.pop(0))
            self._return_list_to_cube(temp, index, axis, j)

    def finish_turning_whole_cube(self, axis: int, clockwise: bool):
        self.turning = False
        self.turningWholeCube = False
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    block = self.blocks[i][j][k]
                    if block.numberOfColors == 0:
                        continue
                    block.rotate(axis, clockwise)

        for k in range(self.size):
            self.cycleLists = self._get_all_blocks_to_rotate(k, axis)
            for j, temp in enumerate(self.cycleLists):
                for i in range(self.size - 1 - j * 2):
                    if not clockwise:
                        temp.insert(0, temp.pop())
                    else:
                        temp.append(temp.pop(0))
                self._return_list_to_cube(temp, k, axis, j)

    def _get_all_blocks_to_rotate(self, index, axis) -> list:
        temp = []
        if index % (self.size - 1) == 0:
            for i in range((self.size + 1) // 2):
                row = list(self._get_list(index, axis, i))
                temp.append(row)
        else:
            row = list(self._get_list(index, axis, 0))
            temp.append(row)

        return temp

    def _return_list_to_cube(self, l1st: list, index: int, axis: int, list_number: int):
        size = self.size - 2 * list_number

        if axis == 0:
            i = index
            k = 0
            for j in range(size):
                self.blocks[i][j + list_number][k + list_number] = l1st.pop(0).copy()
            j = size - 1
            for k in range(1, size):
                self.blocks[i][j + list_number][k + list_number] = l1st.pop(0).copy()
            k = size - 1
            for j in range(size - 2, -1, -1):
                self.blocks[i][j + list_number][k + list_number] = l1st.pop(0).copy()
            j = 0
            for k in range(size - 2, 0, -1):
                self.blocks[i][j + list_number][k + list_number] = l1st.pop(0).copy()

        elif axis == 1:
            j = index
            i = 0
            for k in range(size):
                self.blocks[i + list_number][j][k + list_number] = l1st.pop(0).copy()
            k = size - 1
            for i in range(1, size):
                self.blocks[i + list_number][j][k + list_number] = l1st.pop(0).copy()
            i = size - 1
            for k in range(size - 2, -1, -1):
                self.blocks[i + list_number][j][k + list_number] = l1st.pop(0).copy()
            k = 0
            for i in range(size - 2, 0, -1):
                self.blocks[i + list_number][j][k + list_number] = l1st.pop(0).copy()

        elif axis == 2:
            k = index
            j = 0
            for i in range(size):
                self.blocks[i + list_number][j + list_number][k] = l1st.pop(0).copy()
            i = size - 1
            for j in range(1, size):
                self.blocks[i + list_number][j + list_number][k] = l1st.pop(0).copy()
            j = size - 1
            for i in range(size - 2, -1, -1):
                self.blocks[i + list_number][j + list_number][k] = l1st.pop(0).copy()
            i = 0
            for j in range(size - 2, 0, -1):
                self.blocks[i + list_number][j + list_number][k] = l1st.pop(0).copy()

        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.blocks[i][j][k].position = np.array([i, j, k])

    def _get_list(self, index: int, axis: int, list_number: int):
        size = self.size - list_number * 2

        if axis == 0:
            i = index
            k = 0
            for j in range(size):
                yield self.blocks[i][j + list_number][k + list_number]
            j = size - 1
            for k in range(1, size):
                yield self.blocks[i][j + list_number][k + list_number]
            k = size - 1
            for j in range(size - 2, -1, -1):
                yield self.blocks[i][j + list_number][k + list_number]
            j = 0
            for k in range(size - 2, 0, -1):
                yield self.blocks[i][j + list_number][k + list_number]

        elif axis == 1:
            j = index
            i = 0
            for k in range(size):
                yield self.blocks[i + list_number][j][k + list_number]
            k = size - 1
            for i in range(1, size):
                yield self.blocks[i + list_number][j][k + list_number]
            i = size - 1
            for k in range(size - 2, -1, -1):
                yield self.blocks[i + list_number][j][k + list_number]
            k = 0
            for i in range(size - 2, 0, -1):
                yield self.blocks[i + list_number][j][k + list_number]

        elif axis == 2:
            k = index
            j = 0
            for i in range(size):
                yield self.blocks[i + list_number][j + list_number][k]
            i = size - 1
            for j in range(1, size):
                yield self.blocks[i + list_number][j + list_number][k]
            j = size - 1
            for i in range(size - 2, -1, -1):
                yield self.blocks[i + list_number][j + list_number][k]
            i = 0
            for j in range(size - 2, 0, -1):
                yield self.blocks[i + list_number][j + list_number][k]

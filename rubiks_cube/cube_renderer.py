import math

import OpenGL.GL.shaders as shaders
import numpy as np
import pyrr as pr
from OpenGL.GL import *

from rubiks_cube.rubiks_cube import RubiksCube

with open("shaders/cube_vertex.glsl") as f:
    VERTEX_SHADER = f.read()

with open("shaders/cube_fragment.glsl") as f:
    FRAGMENT_SHADER = f.read()

COLORS = [
    pr.Vector3([1.0, 1.0, 0.0]),
    pr.Vector3([0.0, 1.0, 0.0]),
    pr.Vector3([0.0, 1.0, 0.0]),
    pr.Vector3([0.0, 0.0, 1.0]),
    pr.Vector3([1.0, 0.0, 0.0]),
    pr.Vector3([1.0, 0.5, 0.0]),
    pr.Vector3([1.0, 0.0, 1.0])
]


class CubeRenderer:
    """
    Класс, занимающийся отрисовкой Кубика Рубика используя OpenGL
    """

    def __init__(self):
        # Шейдеры - программы, исполняемые GPU
        # Они работают намного быстрей идентичных на CPU
        # В данном случае шейдер определяет позицию вершин всех блкоков куба и дает им цвета
        self.shader = shaders.compileProgram(shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
                                             shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER))
        # Uniform variables - способо передачи данных в шейдер из исполняемой программы
        self.uniformLocations = {
            # ProjectionMatrix отвечает за генерацию проекции 3D моделей на 2D экран
            "u_ProjectionMatrix":     glGetUniformLocation(self.shader, "u_ProjectionMatrix"),
            # ViewMatrix - transformationMatrix камеры
            "u_ViewMatrix":           glGetUniformLocation(self.shader, "u_ViewMatrix"),
            # Transformation matrix - позиция, вращение, размер обьекта
            "u_TransformationMatrix": glGetUniformLocation(self.shader, "u_TransformationMatrix"),
            "u_FaceColor":            glGetUniformLocation(self.shader, "u_FaceColor"),
            "u_LightColor":           glGetUniformLocation(self.shader, "u_LightColor"),
            "u_LightPosition":        glGetUniformLocation(self.shader, "u_LightPosition"),
        }
        # 8 вершин куба
        cube_vertices = np.array([1., 1., -1.,
                                  1., -1., -1.,
                                  1., 1., 1.,
                                  1., -1., 1.,
                                  -1., 1., -1.,
                                  -1., -1., -1.,
                                  -1., 1., 1.,
                                  -1.0, -1., 1., ],
                                 np.float32)
        # Индексы рисования сторон
        cube_indices = np.array([5, 7, 3, 5, 3, 1,
                                 0, 2, 6, 0, 6, 4,
                                 5, 4, 6, 5, 6, 7,
                                 3, 2, 0, 3, 0, 1,
                                 1, 0, 4, 1, 4, 5,
                                 7, 6, 2, 7, 2, 3], np.uint32)

        # VertexArrayObject - обеькт в памяти видеокарты, хранящий данные о 3D обеькте
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        # У VAO есть Buffers - вершины, индексы, аттрибуты
        vertices_vbo = glGenBuffers(1)  # Обьект для хранения вершин
        glBindBuffer(GL_ARRAY_BUFFER, vertices_vbo)
        glBufferData(GL_ARRAY_BUFFER, 96, cube_vertices, GL_STATIC_DRAW)

        indices_ebo = glGenBuffers(1)  # Обьект для хранения индексов
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indices_ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, cube_indices, GL_STATIC_DRAW)

        # Аттрибут позиции - то, что передается в шейдер автоматически на каждую из вершин
        # В данном случае - позиции вершины
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)

    def render(self, cube: RubiksCube, camera, light):
        glUseProgram(self.shader)  # Используем шейдер
        glBindVertexArray(self.vao)  # Используем модель куба
        glUniformMatrix4fv(self.uniformLocations["u_ProjectionMatrix"], 1, GL_FALSE, camera.projectionMatrix)
        glUniformMatrix4fv(self.uniformLocations["u_ViewMatrix"], 1, GL_FALSE, camera.viewMatrix)
        glUniform3fv(self.uniformLocations["u_LightPosition"], 1, light.position)
        glUniform3fv(self.uniformLocations["u_LightColor"], 1, light.color)

        for row in cube.blocks:
            for col in row:
                for block in col:
                    # Считаем transformation_matrix исходя из позиции блока в кубе (2 - размер одного блока)
                    transformation_matrix = pr.matrix44.create_from_translation(cube.offset + block.position * 2)
                    if cube.turning and (cube.turningWholeCube or block in cube.rotatingBlocks):
                        if cube.rotationAxis == 0:
                            rot = pr.matrix44.create_from_x_rotation(math.radians(cube.rotationAngle))
                        elif cube.rotationAxis == 1:
                            rot = pr.matrix44.create_from_y_rotation(math.radians(cube.rotationAngle))
                        else:
                            rot = pr.matrix44.create_from_z_rotation(math.radians(cube.rotationAngle))
                        transformation_matrix = pr.matrix44.multiply(transformation_matrix, rot)

                    # Передаем юниформ в шейдер
                    glUniformMatrix4fv(self.uniformLocations["u_TransformationMatrix"],
                                       1, GL_FALSE, transformation_matrix)
                    # Рисуем каждую из сторон индивидуально, передвавая их цвет
                    for i in range(6):
                        glUniform3fv(self.uniformLocations["u_FaceColor"], 1, COLORS[block.facesColors[i]])
                        ptr = ctypes.c_void_p(i * 4 * 6)  # (void*)(i * 6 * sizeof(float))
                        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, ptr)

        glBindVertexArray(0)
        glUseProgram(0)

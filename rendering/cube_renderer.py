import math

import OpenGL.GL.shaders as shaders
import numpy as np
import pyrr as pr
from OpenGL.GL import *

from rubiks_cube.rubiks_cube import RubiksCube

CUBE_VERTEX_SHADER = """
#version %d%d0

layout(location = 0) in vec3 in_Pos;

out vec3 pass_SurfaceNormal;
out vec3 pass_ToCameraVector;
out vec3 pass_ToLightVector;

uniform vec3 u_LightPosition;
uniform vec3 u_FaceNormal;

uniform mat4 u_TransformationMatrix;
uniform mat4 u_ProjectionMatrix;
uniform mat4 u_ViewMatrix;

void main()
{
    vec4 worldPosition = u_TransformationMatrix * vec4(in_Pos, 1.0);
    gl_Position = u_ProjectionMatrix * u_ViewMatrix * worldPosition;

    pass_SurfaceNormal = (u_TransformationMatrix * vec4(u_FaceNormal, 0.0)).xyz;
    pass_ToLightVector = u_LightPosition - worldPosition.xyz;
    pass_ToCameraVector = (inverse(u_ViewMatrix) * vec4(0.0, 0.0, 0.0, 1.0)).xyz - worldPosition.xyz;
}"""

CUBE_FRAGMENT_SHADER = """
#version %d%d0

in vec3 pass_SurfaceNormal;
in vec3 pass_ToCameraVector;
in vec3 pass_ToLightVector;

out vec4 out_Color;

uniform vec3 u_LightColor;
uniform vec3 u_FaceColor;

uniform float u_Reflectivity;
uniform float u_ColorFactor;

void main()
{
    if (u_FaceColor == vec3(0.0)) { out_Color = vec4(0.0, 0.0, 0.0, 1.0); return; } 

    vec3 unitNormal = normalize(pass_SurfaceNormal);
    vec3 unitLightVector = normalize(pass_ToLightVector);

    vec3 diffuse = vec3(u_ColorFactor);

    vec3 unitVectorToCamera = normalize(pass_ToCameraVector);
    vec3 lightDirection = -unitLightVector;
    vec3 reflectedLightDirection = reflect(lightDirection, unitNormal);

    float specularFactor = max(dot(reflectedLightDirection, unitVectorToCamera), 0.0);
    float dampedFactor = pow(specularFactor, 1);

    vec3 finalSpecular = dampedFactor * u_Reflectivity * u_LightColor;

    out_Color = vec4(diffuse, 1.0) * vec4(u_FaceColor, 1.0) + vec4(finalSpecular, 1.0);
}
"""

COLORS = [
    pr.Vector3([0.0, 0.0, 0.0]),
    pr.Vector3([1.0, 1.0, 1.0]),
    pr.Vector3([1.0, 1.0, 0.0]),
    pr.Vector3([0.0, 1.0, 0.0]),
    pr.Vector3([0.0, 0.0, 1.0]),
    pr.Vector3([1.0, 0.0, 0.0]),
    pr.Vector3([1.0, 0.5, 0.0])
]

NORMALS = [
    pr.Vector3([0.0, -1.0, 0.0]),
    pr.Vector3([0.0, 1.0, 0.0]),
    pr.Vector3([-1.0, 0.0, 0.0]),
    pr.Vector3([1.0, 0.0, 0.0]),
    pr.Vector3([0.0, 0.0, -1.0]),
    pr.Vector3([0.0, 0.0, 1.0]),
]


class CubeRenderer:
    """
    Класс, занимающийся отрисовкой Кубика Рубика используя OpenGL
    """

    def __init__(self):
        # 8 вершин куба
        cube_vertices = np.array([1.0, 1.0, -1.0,
                                  1.0, -1.0, -1.0,
                                  1.0, 1.0, 1.0,
                                  1.0, -1.0, 1.0,
                                  -1.0, 1.0, -1.0,
                                  -1.0, -1.0, -1.0,
                                  -1.0, 1.0, 1.0,
                                  -1.0, -1.0, 1.0, ], np.float32)

        # VertexArrayObject - обеькт в памяти видеокарты, хранящий данные о 3D обеькте
        self.cubeVao = glGenVertexArrays(1)
        glBindVertexArray(self.cubeVao)
        # У VAO есть Buffers - вершины, индексы, аттрибуты
        vertices_vbo = glGenBuffers(1)  # Обьект для хранения вершин
        glBindBuffer(GL_ARRAY_BUFFER, vertices_vbo)
        glBufferData(GL_ARRAY_BUFFER, 96, cube_vertices, GL_STATIC_DRAW)
        indices_ebo = glGenBuffers(1)  # Обьект для хранения индексов
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indices_ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, np.array([5, 7, 3, 5, 3, 1,
                                                             0, 2, 6, 0, 6, 4,
                                                             5, 4, 6, 5, 6, 7,
                                                             3, 2, 0, 3, 0, 1,
                                                             1, 0, 4, 1, 4, 5,
                                                             7, 6, 2, 7, 2, 3], np.uint32),
                     GL_STATIC_DRAW)
        # Аттрибут - то, что передается в шейдер автоматически на каждую из вершин
        # В данном случае - позиции вершины
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindVertexArray(0)
        self.outlineVao = glGenVertexArrays(1)
        glBindVertexArray(self.outlineVao)
        glBindBuffer(GL_ARRAY_BUFFER, vertices_vbo)  # Используем буффер вершин второй раз
        outline_indices_ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, outline_indices_ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 96, np.array([5, 7, 7, 3, 3, 1, 1, 5,  # Верхняя сторона
                                                            4, 6, 6, 2, 2, 0, 0, 4,  # Нижняя сторона
                                                            7, 6,
                                                            5, 4,
                                                            1, 0,
                                                            3, 2], np.uint32),
                     GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        major = glGetInteger(GL_MAJOR_VERSION)
        minor = glGetInteger(GL_MINOR_VERSION)
        # Шейдеры - программы, исполняемые GPU
        # Они работают намного быстрей идентичных на CPU
        # В данном случае шейдер определяет позицию вершин всех блкоков куба и дает им цвета
        # NOTE: по некоторой причине на MacOS Qt не может запросить нужную версию OpenGL - форматирую код под нужную
        # NOTE: в некоторых версиях OpenGL шейдер не может быть скомпилирован без привязанного VertexArray
        self.cubeShader = shaders.compileProgram(shaders.compileShader(CUBE_VERTEX_SHADER % (major, minor),
                                                                       GL_VERTEX_SHADER),
                                                 shaders.compileShader(CUBE_FRAGMENT_SHADER % (major, minor),
                                                                       GL_FRAGMENT_SHADER))
        # Uniform variables - способо передачи данных в шейдер из исполняемой программы
        self.cubeUniformLocations = {
            "u_ProjectionMatrix":     glGetUniformLocation(self.cubeShader, "u_ProjectionMatrix"),
            "u_ViewMatrix":           glGetUniformLocation(self.cubeShader, "u_ViewMatrix"),
            "u_TransformationMatrix": glGetUniformLocation(self.cubeShader, "u_TransformationMatrix"),
            "u_FaceColor":            glGetUniformLocation(self.cubeShader, "u_FaceColor"),
            "u_LightColor":           glGetUniformLocation(self.cubeShader, "u_LightColor"),
            "u_LightPosition":        glGetUniformLocation(self.cubeShader, "u_LightPosition"),
            "u_Reflectivity":         glGetUniformLocation(self.cubeShader, "u_Reflectivity"),
            "u_FaceNormal":           glGetUniformLocation(self.cubeShader, "u_FaceNormal"),
            "u_ColorFactor":          glGetUniformLocation(self.cubeShader, "u_ColorFactor"),
        }
        glUseProgram(self.cubeShader)
        glUniformMatrix4fv(self.cubeUniformLocations["u_ViewMatrix"], 1, GL_FALSE, pr.Matrix44.identity())

        glBindVertexArray(0)

    def render(self, cube: RubiksCube, proj_mat: pr.Matrix44, view_mat: pr.Matrix44,
               light_col: pr.Vector3, light_pos: pr.Vector3,
               reflectivity: float, diffuse_factor: float):
        glUseProgram(self.cubeShader)  # Используем один шейдер на весь куб

        glUniformMatrix4fv(self.cubeUniformLocations["u_ProjectionMatrix"], 1, GL_FALSE, proj_mat)
        glUniform3fv(self.cubeUniformLocations["u_LightPosition"], 1, light_pos)
        glUniform3fv(self.cubeUniformLocations["u_LightColor"], 1, light_col)
        glUniform1f(self.cubeUniformLocations["u_Reflectivity"], reflectivity)
        glUniform1f(self.cubeUniformLocations["u_ColorFactor"], diffuse_factor)

        for row in cube.blocks:
            for col in row:
                for block in col:
                    if block.numberOfColors == 0:
                        continue

                    # Считаем transformation_matrix исходя из позиции блока в кубе (2 - размер одного блока)
                    transformation_matrix = pr.matrix44.create_from_translation(cube.offset + block.position * 2)
                    transformation_matrix = pr.matrix44.multiply(transformation_matrix,
                                                                 pr.matrix44.create_from_scale(cube.blockSize))
                    if cube.turning and (cube.turningWholeCube or block in cube.rotatingBlocks):
                        rot_coef = 1 if cube.turningClockwise else -1
                        if cube.rotationAxis == 0:
                            rot = pr.matrix44.create_from_x_rotation(math.radians(cube.rotationAngle) * rot_coef)
                        elif cube.rotationAxis == 1:
                            rot = pr.matrix44.create_from_y_rotation(math.radians(cube.rotationAngle) * rot_coef)
                        else:
                            rot = pr.matrix44.create_from_z_rotation(math.radians(cube.rotationAngle) * rot_coef)
                        transformation_matrix = pr.matrix44.multiply(transformation_matrix, rot)
                    transformation_matrix = pr.matrix44.multiply(transformation_matrix, view_mat)

                    glUniformMatrix4fv(self.cubeUniformLocations["u_TransformationMatrix"],
                                       1, GL_FALSE, transformation_matrix)
                    # Отрисовка сторон куба
                    glBindVertexArray(self.cubeVao)
                    for i in range(6):  # Рисуем каждую из сторон индивидуально, передвавая их цвет
                        color = block.facesColors[i]
                        if color == 0 and not cube.turning:
                            continue

                        glUniform3fv(self.cubeUniformLocations["u_FaceNormal"], 1, NORMALS[i])
                        glUniform3fv(self.cubeUniformLocations["u_FaceColor"], 1, COLORS[color])
                        ptr = ctypes.c_void_p(i * 6 * 4)  # (void*)(i * 6 * sizeof(float))
                        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, ptr)
                    # Отрисовка внешней линии
                    glBindVertexArray(self.outlineVao)
                    glUniform3fv(self.cubeUniformLocations["u_FaceColor"], 1, COLORS[0])
                    glDrawElements(GL_LINES, 24, GL_UNSIGNED_INT, None)

        glBindVertexArray(0)

import glfw
import pyrr as pr
from OpenGL.GL import *

from camera import Camera
from rubiks_cube.cube_renderer import CubeRenderer
from rubiks_cube.rubiks_cube import RubiksCube
from utils import Light
from window import Window


def configure_opengl():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)
    glLineWidth(2)


def main():
    window = Window(1000, 1000, "Rubiks Cube")
    camera = Camera(window)

    light = Light(pr.Vector3([0.0, .0, -10]), pr.Vector3([1.0, 1.0, 1.0]))

    cube = RubiksCube(3)
    renderer = CubeRenderer()

    configure_opengl()

    while not window.close_button_pressed():
        window.clear()

        camera.move()
        cube.update()

        if window.keyboard.is_key_pressed(glfw.KEY_G):
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        elif window.keyboard.is_key_released(glfw.KEY_G):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        if window.keyboard.is_key_pressed(glfw.KEY_R):
            cube.turn_cube(0, 0, True)

        renderer.render(cube, camera, light)

        window.update()


if __name__ == '__main__':
    main()

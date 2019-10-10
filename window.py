import glfw
from OpenGL.GL import *


class Keyboard:
    def __init__(self):
        self.heldButtons = set()
        self.pressedButtonsThisFrame = set()
        self.releasedButtonsThisFrame = set()

    def update(self):
        self.pressedButtonsThisFrame.clear()
        self.releasedButtonsThisFrame.clear()

    def add_keyboard_listener(self, window_id):
        def func(window, key, scancode, action, mods):
            if action == glfw.PRESS:
                self.report_key_press(key)
            elif action == glfw.RELEASE:
                self.report_key_release(key)

        glfw.set_key_callback(window_id, func)

    def report_key_press(self, key):
        self.pressedButtonsThisFrame.add(key)
        self.heldButtons.add(key)

    def report_key_release(self, key):
        self.releasedButtonsThisFrame.add(key)
        self.heldButtons.remove(key)

    def is_key_pressed(self, key):
        return key in self.pressedButtonsThisFrame

    def is_key_released(self, key):
        return key in self.releasedButtonsThisFrame

    def is_key_held(self, key):
        return key in self.heldButtons


class Mouse:
    def __init__(self, window):
        self.heldButtons = set()
        self.pressedButtonsThisFrame = set()
        self.releasedButtonsThisFrame = set()

        self.window = window

        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.lastX = 0
        self.lastY = 0
        self.scroll = 0

        self.add_click_listener()
        self.add_move_listener(window.id)
        self.add_scroll_listener()

    def update(self):
        self.pressedButtonsThisFrame.clear()
        self.releasedButtonsThisFrame.clear()
        self.dx = self.lastX - self.x
        self.dy = self.lastY - self.y
        self.lastX = self.x
        self.lastY = self.y

    def add_move_listener(self, window_id):
        def func(window, x_pos, y_pos):
            self.x = float(x_pos / self.window.screenWidth)
            self.y = float(y_pos / self.window.screenHeight)

        glfw.set_cursor_pos_callback(window_id, func)

    def add_click_listener(self):
        def func(window, button, action, mods):
            if action == glfw.PRESS:
                self.report_key_press(button)
            elif action == glfw.RELEASE:
                self.report_key_release(button)

        glfw.set_mouse_button_callback(self.window.id, func)

    def add_scroll_listener(self):
        def func(window, x_offset, y_offset):
            self.scroll = float(y_offset)

        glfw.set_scroll_callback(self.window.id, func)

    def report_key_press(self, key):
        self.pressedButtonsThisFrame.add(key)
        self.heldButtons.add(key)

    def report_key_release(self, key):
        self.releasedButtonsThisFrame.add(key)
        self.heldButtons.remove(key)

    def is_key_pressed(self, key):
        return key in self.pressedButtonsThisFrame

    def is_key_released(self, key):
        return key in self.releasedButtonsThisFrame

    def is_key_held(self, key):
        return key in self.heldButtons


class Window:

    def __init__(self, width, height, title):
        if not glfw.init():
            raise RuntimeError("Failed to init glfw")

        self.id = glfw.create_window(width, height, title, None, None)
        self.screenWidth = width
        self.screenHeight = height

        if not self.id:
            raise RuntimeError("Failed to create window")

        glfw.make_context_current(self.id)
        # glfw.swap_interval(1)
        glfw.show_window(self.id)

        glfw.set_window_size_callback(self.id, lambda win, w, h: glViewport(0, 0, w, h))

        self.keyboard = Keyboard()
        self.keyboard.add_keyboard_listener(self.id)
        self.mouse = Mouse(self)

    def update(self):
        self.mouse.update()
        self.keyboard.update()
        glfw.swap_buffers(self.id)
        glfw.poll_events()

    @staticmethod
    def clear():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def close_button_pressed(self):
        return glfw.window_should_close(self.id)

    @property
    def ratio(self) -> float:
        return self.screenWidth / self.screenHeight

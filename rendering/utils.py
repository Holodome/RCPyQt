import pyrr as pr


# Класс для более плавных вращений и приближения камеры
class SmoothFloat:
    def __init__(self, init_value, agility):
        self.actual = init_value
        self.target = init_value
        self.agility = agility

    def update(self, delta):
        offset = self.target - self.actual
        change = offset * delta * self.agility
        self.actual += change


class Light:

    def __init__(self, position: pr.Vector3, color: pr.Vector3):
        self.position = position
        self.color = color

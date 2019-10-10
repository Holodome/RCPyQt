import dataclasses

import pyrr as pr


class SmoothFloat:
    def __init__(self, init_value, agility):
        self.actual = init_value
        self.target = init_value
        self.agility = agility

    def update(self, delta):
        offset = self.target - self.actual
        change = offset * delta * self.agility
        self.actual += change


@dataclasses.dataclass
class Light:
    position: pr.Vector3
    color: pr.Vector3

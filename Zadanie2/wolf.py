import math
import sheep
import logging


class Wolf:
    def __init__(self, movement):

        self.movement = movement
        self.position = [0.0, 0.0]

    def calc_distance(self, sheep):
        return math.sqrt((sheep.position[0] - self.position[0]) ** 2 + (sheep.position[1] - self.position[1]) ** 2)

    def eat(self, sheep):
        self.position = sheep.position
        sheep.is_alive = False

    def chase(self, sheep):
        dx = sheep.position[0] - self.position[0]
        dy = sheep.position[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        self.position[0] += self.movement * (dx / distance)
        self.position[1] += self.movement * (dy / distance)

    def move(self, sheeps):
        distances = []

        for sheep in sheeps:
            if sheep.is_alive:
                distances.append([sheep, self.calc_distance(sheep)])

        nearest_sheep = min(distances, key=lambda x: x[1])
        logging.debug(f'Wolf chose the nearest sheep. Sheep number {sheeps.index(nearest_sheep[0]) + 1}, at distance {nearest_sheep[1]}')

        if self.calc_distance(nearest_sheep[0]) <= self.movement:
            self.eat(nearest_sheep[0])
            logging.info(f'Wolf moved.')
            logging.debug(f'Wolf moved to position ({self.position[0]}; {self.position[1]}).')
            return True, sheeps.index(nearest_sheep[0]) + 1

        self.chase(nearest_sheep[0])
        logging.info(f'Wolf moved.')
        logging.debug(f'Wolf moved to position ({self.position[0]}; {self.position[1]}).')
        return False, sheeps.index(nearest_sheep[0]) + 1

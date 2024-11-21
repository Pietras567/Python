import math
import sheep

class wolf:
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

    def round(self, sheeps):
        distances = []

        for sheep in sheeps:
            if sheep.is_alive and self.calc_distance(sheep) <= self.movement:
                #print(sheeps.index(sheep) + 1)
                #print(sheep.is_alive)
                self.eat(sheep)
                #print(sheeps.index(sheep) + 1)
                #print(sheep.is_alive)
                return True, sheeps.index(sheep)
            elif sheep.is_alive:
                distances.append([sheep, self.calc_distance(sheep)])
                #print('dodaje')


        nearest_sheep = min(distances, key=lambda x: x[1])
        self.chase(nearest_sheep[0])
        return False, sheeps.index(nearest_sheep[0])

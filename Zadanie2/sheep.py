import random

class sheep:
    def __init__(self, movement, position):

        self.movement = movement
        self.position = position
        self.is_alive = True

    def __str__(self):
        return super().__str__()

    def move(self, all_sheeps, wolf_position):
        directions = ['north', 'south', 'east', 'west']
        random.shuffle(directions)

        for direction in directions:
            potential_position = self.position[:]

            if direction == 'north':
                potential_position[1] += self.movement
            elif direction == 'south':
                potential_position[1] -= self.movement
            elif direction == 'east':
                potential_position[0] += self.movement
            elif direction == 'west':
                potential_position[0] -= self.movement

            if (not any(sheep.position == potential_position for sheep in all_sheeps if sheep.is_alive)
                and not (potential_position == wolf_position)):
                self.position = potential_position
                return

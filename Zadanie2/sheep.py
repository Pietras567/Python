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
        tried_directions = set()
        new_position = self.position[:]

        while len(tried_directions) < len(directions):
            choice = random.choice(directions)
            if choice in tried_directions:
                continue

            #print(all_sheeps.index(self))
            #print(choice)

            tried_directions.add(choice)
            potential_position = new_position[:]

            if choice == 'north':
                potential_position[1] += self.movement
            elif choice == 'south':
                potential_position[1] -= self.movement
            elif choice == 'east':
                potential_position[0] += self.movement
            elif choice == 'west':
                potential_position[0] -= self.movement

            if not any(sheep.position == potential_position for sheep in all_sheeps if sheep.is_alive) and not (potential_position == wolf_position):
                self.position = potential_position
                return

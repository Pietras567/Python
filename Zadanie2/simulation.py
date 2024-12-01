from sheep import Sheep
from wolf import Wolf
import json
import csv
import random
import keyboard
import time
import logging


class Simulation:
    def __init__(self, rounds, sheeps_no, coord_limit, sheep_mov, wolf_mov, need_to_wait):

        self.rounds = rounds
        self.sheeps_no = sheeps_no
        self.coord_limit = coord_limit
        self.sheep_mov = sheep_mov
        self.wolf_mov = wolf_mov
        self.sheeps = []
        self.wolf = Wolf(self.wolf_mov)
        self.need_to_wait = need_to_wait
        self.logs = []
        self.alive = []
        self.initiate_positions()

    def initiate_positions(self):
        for i in range(self.sheeps_no):
            while True:
                position = [random.uniform(-self.coord_limit, self.coord_limit),
                            random.uniform(-self.coord_limit, self.coord_limit)]
                if not any(other_sheep.position == position for other_sheep in self.sheeps):
                    new_sheep = Sheep(self.sheep_mov, position)
                    logging.debug(f'Initial position of the sheep number {i + 1} is: '
                                  f'({new_sheep.position[0]}; {new_sheep.position[1]}).')
                    self.sheeps.append(new_sheep)
                    break

        logging.info(f'Initial positions of all sheep were determined.')

    def print_round_info(self, round_no, ate, sheep_id):
        alive_sheeps = sum(sheep.is_alive for sheep in self.sheeps)
        msg = f'Wolf ate sheep no. {sheep_id}' if ate else f'Wolf is chasing sheep no. {sheep_id}'
        print(f'Round no. {round_no}, Wolf position: ({round(self.wolf.position[0], 3)}, '
              f'{round(self.wolf.position[1], 3)}), No. of sheeps alive: {alive_sheeps}, {msg}')

    def simulate(self):
        for i in range(self.rounds):
            logging.info(f'Round number {i + 1} started.')
            if sum(sheep.is_alive for sheep in self.sheeps) == 0:
                logging.info(f'All sheep have been eaten. End of simulation.')
                return
            self.round_algorithm(i)
        logging.info(f'Predefined maximum number of rounds has been reached. End of simulation.')

    def round_algorithm(self, round_no):
        for sheep in self.sheeps:
            if sheep.is_alive:
                sheep.move(self.sheeps, self.wolf.position)

        logging.info(f'All alive sheep finished moving.')

        ate, sheep_id = self.wolf.move(self.sheeps)

        logging.info(f'Wolf ate sheep no. {sheep_id}') if ate else logging.info(f'Wolf is chasing sheep no. {sheep_id}')

        self.print_round_info(round_no + 1, ate, sheep_id)
        self.logs_to_file(round_no + 1)
        self.alive_no_to_csv(round_no + 1)
        logging.info(f'Round number {round_no + 1} finished. '
                     f'Number of alive sheep: {sum(sheep.is_alive for sheep in self.sheeps)}.')

        if self.need_to_wait:
            keyboard.read_key()
            time.sleep(0.15)

    def prepare_log(self, round_no):
        data = {
            "round_no": round_no,
            "wolf_pos": self.wolf.position,
            "sheeps_pos": [
                sheep.position if sheep.is_alive else None for sheep in self.sheeps
            ]
        }
        return data

    def logs_to_file(self, round_no, filename="pos.json"):
        self.logs.append(self.prepare_log(round_no))
        with open(filename, "w") as file:
            json.dump(self.logs, file, indent=4)

        logging.debug(f'Information was saved to sile {filename}.')

    def alive_no_to_csv(self, round_no, filename="alive.csv"):
        header = ["round_no", "sheeps_alive"]
        data = [round_no, sum(sheep.is_alive for sheep in self.sheeps)]
        self.alive.append(data)

        with open(filename, "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(header)
            writer.writerows(self.alive)

        logging.debug(f'Information was saved to sile {filename}.')

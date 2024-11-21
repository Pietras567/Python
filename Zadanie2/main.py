from simulation import simulation

def main():
    """
    # Parametry symulacji
    rounds = 50
    sheeps_no = 15
    coord_limit = 10.0
    sheep_mov = 0.5
    wolf_mov = 1.0
    """

    rounds = 100
    sheeps_no = 15
    coord_limit = 10.0
    sheep_mov = 0.5
    wolf_mov = 1.0

    sim = simulation(rounds, sheeps_no, coord_limit, sheep_mov, wolf_mov)
    sim.simulate()


if __name__ == '__main__':
    main()


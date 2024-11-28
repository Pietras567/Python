from xmlrpc.client import boolean

from simulation import simulation
import argparse
import configparser

def main():
    parser = argparse.ArgumentParser(description='Symulator wilka i owiec')

    parser.add_argument('-c', '--config', type=str, help='Configuration file location', required=False)
    parser.add_argument('-l', '--log', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Logging level', required=False)
    parser.add_argument('-r', '--rounds', type=int, default=50, help='Number of rounds', required=False)
    parser.add_argument('-s', '--sheep', type=int, default=15, help='Number of sheeps', required=False)
    parser.add_argument('-w', '--wait', action='store_true', help='Wait at the end of each round')

    args = parser.parse_args()

    if args.log not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] and args.log is not None:
        raise ValueError('Logging level must be DEBUG, INFO, WARNING, ERROR, CRITICAL')
    if args.rounds < 0:
        raise ValueError('Number of rounds must be positive')
    if args.sheep < 0:
        raise ValueError('Number of sheeps must be positive')

    log_level = args.log

    if args.config is None:
        rounds = args.rounds
        sheeps_no = args.sheep
        coord_limit = 10.0
        sheep_mov = 0.5
        wolf_mov = 1.0

        sim = simulation(rounds, sheeps_no, coord_limit, sheep_mov, wolf_mov, True if args.wait else False, log_level if args.log is not None else None)
        sim.simulate()
    else:
        rounds = args.rounds
        sheeps_no = args.sheep

        config = configparser.ConfigParser()
        config.read(args.config)

        coord_limit = abs(float(config.get('Sheep', 'InitPosLimit')))
        sheep_mov = float(config.get('Sheep', 'MoveDist'))
        wolf_mov = float(config.get('Wolf', 'MoveDist'))

        if sheep_mov < 0:
            raise ValueError('Sheeps movement speed must be positive')
        if wolf_mov < 0:
            raise ValueError('Wolf movement speed must be positive')

        sim = simulation(rounds, sheeps_no, coord_limit, sheep_mov, wolf_mov, True if args.wait else False, log_level if args.log is not None else None)
        sim.simulate()




    """
    # Domyślne parametry symulacji
    rounds = 50
    sheeps_no = 15
    coord_limit = 10.0
    sheep_mov = 0.5
    wolf_mov = 1.0
    """

    rounds = 50
    sheeps_no = 15
    coord_limit = 10.0
    sheep_mov = 0.5
    wolf_mov = 1.0

    # sim = simulation(rounds, sheeps_no, coord_limit, sheep_mov, wolf_mov, True if args.wait else False)
    # sim.simulate()


if __name__ == '__main__':
    main()


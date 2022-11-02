import csv
import os
import time

from tqdm import trange

from simulations import SIMULATION_02, SIMULATION_01


def main(n_sims):
    for i in trange(n_sims):
        t_start_sim_1 = time.time()
        SIMULATION_01(60, 180)  # Takes between 1 and 3 minutes to complete
        t_end_sim_1 = time.time()
        t_start_sim_2 = time.time()
        SIMULATION_02(60, 180)  # Takes between 1 and 3 minutes to complete, beta dist
        t_end_sim_2 = time.time()
        log_data(i, t_end_sim_1 - t_start_sim_1,
                 t_end_sim_2 - t_start_sim_2,
                 file="./results/results.csv")


def log_data(i, sim1_time, sim2_time, file):
    header = ["i", "sim1_time", "sim2_time", "delta"]
    row = [i, sim1_time, sim2_time, sim1_time - sim2_time]
    automkdir(file)
    if os.path.exists(file):
        header = False
    with open(file, 'a', newline='') as logfile:
        writer = csv.writer(logfile)
        if header:
            writer.writerow(header)
        writer.writerow(row)
    pass


def automkdir(filename):
    """Automatically makes the folders needed"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)


if __name__ == '__main__':
    main(10)

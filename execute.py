import argparse
import time
from importlib import import_module

import numpy as np
from qm import QuantumMachinesManager, SimulationConfig, generate_qua_script, qua
from qm.octave import QmOctaveConfig
from qm.simulate.credentials import create_credentials
from qualang_tools.simulator_tools import create_simulator_controller_connections

HOST = "192.168.0.101"
PORT = 80

parser = argparse.ArgumentParser()
parser.add_argument("program")
parser.add_argument("-s", "--simulate", action="store_true")
parser.add_argument("--duration", default=5000)


class Controller:

    def __init__(self, cloud=False):
        credentials = None
        if cloud:
            credentials = create_credentials()
        self.manager = QuantumMachinesManager(
            host=HOST, port=PORT, credentials=credentials
        )

    def simulate(self, config, prog, duration):
        ncontrollers = len(config["controllers"])
        controller_connections = create_simulator_controller_connections(ncontrollers)
        simulation_config = SimulationConfig(
            duration=duration,
            controller_connections=controller_connections,
        )
        return self.manager.simulate(config, prog, simulation_config)

    def execute(self, config, prog):
        manager = QuantumMachinesManager(host=HOST, port=PORT)
        machine = self.manager.open_qm(config)
        return machine.execute(prog)


def fetch(result):
    handles = result.result_handles
    handles.wait_for_all_values()
    return {k: v.fetch_all() for k, v in handles.items()}


def main(program, simulate, duration):
    module = import_module(f"programs.{program}")
    prog = module.prog
    config = module.config

    if simulate:
        result = simulate(config, prog, duration=5000)
        samples = result.get_simulated_samples()
        np.save("data.npy", samples.con3.analog)
        return

    start_time = time.time()
    controller = Controller()
    conn_time = time.time() - start_time
    print("Connection time:", conn_time)

    start_time = time.time()
    result = controller.execute(config, prog)
    exec_time = time.time() - start_time
    print("Execution time:", exec_time)

    start_time = time.time()
    data = fetch(result)
    fetch_time = time.time() - start_time
    for k, v in data.items():
        print(k, v.shape)
    print("Fetch time:", fetch_time)

    print("Total time:", conn_time + exec_time + fetch_time)


if __name__ == "__main__":
    args = parser.parse_args()
    main(**vars(args))

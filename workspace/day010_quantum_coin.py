from math import asin, sqrt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def quantum_coin(
    shots: int = 1000,
    probability_one: float = 0.5,
    seed: int = 10,
):
    if not 0 <= probability_one <= 1:
        raise ValueError("probability_one must be between 0 and 1")

    theta = 2 * asin(sqrt(probability_one))
    circuit = QuantumCircuit(1, 1)
    circuit.ry(theta, 0)
    circuit.measure(0, 0)

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator, seed_transpiler=seed)
    counts = simulator.run(
        compiled, shots=shots, seed_simulator=seed
    ).result().get_counts()
    return circuit, counts


if __name__ == "__main__":
    _, fair_counts = quantum_coin()
    _, weighted_counts = quantum_coin(probability_one=0.7)
    print("fair:", fair_counts)
    print("weighted:", weighted_counts)
    assert abs(fair_counts.get("1", 0) / 1000 - 0.5) < 0.08
    assert abs(weighted_counts.get("1", 0) / 1000 - 0.7) < 0.08


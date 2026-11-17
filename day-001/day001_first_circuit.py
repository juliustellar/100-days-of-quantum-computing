from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def run_first_circuit(shots: int = 1024, seed: int = 7):
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator, seed_transpiler=seed)
    result = simulator.run(
        compiled, shots=shots, seed_simulator=seed
    ).result()
    return circuit, result.get_counts()


if __name__ == "__main__":
    qc, counts = run_first_circuit()
    print(qc.draw(output="text"))
    print(counts)
    assert set(counts) == {"0", "1"}
    assert sum(counts.values()) == 1024


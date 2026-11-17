from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def phase_oracle(target: str) -> QuantumCircuit:
    if len(target) != 2 or set(target) - {"0", "1"}:
        raise ValueError("target must be a two-bit string")

    oracle = QuantumCircuit(2, name=f"mark {target}")
    for qubit, bit in enumerate(reversed(target)):
        if bit == "0":
            oracle.x(qubit)
    oracle.cz(0, 1)
    for qubit, bit in enumerate(reversed(target)):
        if bit == "0":
            oracle.x(qubit)
    return oracle


def diffuser() -> QuantumCircuit:
    circuit = QuantumCircuit(2, name="diffuser")
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])
    return circuit


def grover_search(target: str = "11", shots: int = 1024, seed: int = 55):
    circuit = QuantumCircuit(2, 2)
    circuit.h([0, 1])
    circuit.compose(phase_oracle(target), inplace=True)
    circuit.compose(diffuser(), inplace=True)
    circuit.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator, seed_transpiler=seed)
    counts = simulator.run(
        compiled, shots=shots, seed_simulator=seed
    ).result().get_counts()
    return circuit, counts


if __name__ == "__main__":
    for target in ["00", "01", "10", "11"]:
        _, counts = grover_search(target)
        print(target, counts)
        assert max(counts, key=counts.get) == target


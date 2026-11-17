from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError, depolarizing_error


def bell_circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def teaching_noise_model() -> NoiseModel:
    model = NoiseModel()
    model.add_all_qubit_quantum_error(
        depolarizing_error(0.02, 1), ["h"]
    )
    model.add_all_qubit_quantum_error(
        depolarizing_error(0.04, 2), ["cx"]
    )
    model.add_all_qubit_readout_error(
        ReadoutError([[0.97, 0.03], [0.05, 0.95]])
    )
    return model


def run_counts(simulator: AerSimulator, shots: int, seed: int):
    circuit = bell_circuit()
    compiled = transpile(circuit, simulator, seed_transpiler=seed)
    return simulator.run(
        compiled, shots=shots, seed_simulator=seed
    ).result().get_counts()


def audit(counts: dict[str, int]) -> dict[str, float]:
    shots = sum(counts.values())
    forbidden = counts.get("01", 0) + counts.get("10", 0)
    correlated = counts.get("00", 0) + counts.get("11", 0)
    return {
        "correlation_rate": correlated / shots,
        "forbidden_rate": forbidden / shots,
        "one_balance": counts.get("11", 0) / max(correlated, 1),
    }


if __name__ == "__main__":
    shots = 2000
    ideal = run_counts(AerSimulator(), shots, seed=100)
    noisy = run_counts(
        AerSimulator(noise_model=teaching_noise_model()), shots, seed=100
    )
    print("ideal", ideal, audit(ideal))
    print("noisy", noisy, audit(noisy))
    assert audit(ideal)["forbidden_rate"] == 0
    assert audit(noisy)["forbidden_rate"] > 0


from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

qc = QuantumCircuit(1, 1); qc.h(0); qc.measure(0, 0)
noise = NoiseModel()
noise.add_all_qubit_quantum_error(
    depolarizing_error(0.02, 1), ["h"])
sim = AerSimulator(noise_model=noise)
result = sim.run(transpile(qc, sim), shots=2000).result()
print(result.get_counts())

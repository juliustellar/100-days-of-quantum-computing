from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0); qc.measure(0, 0)
sim = AerSimulator(seed_simulator=7)
compiled = transpile(qc, sim)
for shots in [10, 100, 1000, 10000]:
    counts = sim.run(compiled, shots=shots).result().get_counts()
    print(shots, counts.get("1", 0) / shots)

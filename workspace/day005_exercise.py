from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(range(1), range(1))
sim = AerSimulator()
compiled = transpile(qc, sim)
counts = sim.run(compiled, shots=1024).result().get_counts()
print(counts)

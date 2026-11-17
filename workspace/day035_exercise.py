from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure(range(2), range(2))
sim = AerSimulator()
compiled = transpile(qc, sim)
counts = sim.run(compiled, shots=1024).result().get_counts()
print(counts)

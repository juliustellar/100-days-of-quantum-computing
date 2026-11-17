from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3, 3)
qc.cx(0, 2)
qc.cx(1, 2)
qc.measure(range(3), range(3))
sim = AerSimulator()
compiled = transpile(qc, sim)
counts = sim.run(compiled, shots=1024).result().get_counts()
print(counts)

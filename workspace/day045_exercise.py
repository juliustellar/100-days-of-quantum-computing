from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0); qc.cx(0, 1); qc.barrier(); qc.cx(0, 1)
compiled = transpile(qc, AerSimulator(), optimization_level=3)
print("depth", compiled.depth())
print("ops", compiled.count_ops())

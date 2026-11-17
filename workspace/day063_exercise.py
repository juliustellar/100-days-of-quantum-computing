from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

qc = QuantumCircuit(3, 2)
qc.x(2); qc.h([0, 1])
qc.cp(3.14159 / 2, 0, 2)
qc.cp(3.14159, 1, 2)
qc.compose(QFT(2, inverse=True), [0, 1], inplace=True)
qc.measure([0, 1], [0, 1])
print(qc)

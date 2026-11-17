from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

marked = "10"
qc = QuantumCircuit(2)
qc.h([0, 1])
for q, bit in enumerate(reversed(marked)):
    if bit == "0": qc.x(q)
qc.cz(0, 1)
for q, bit in enumerate(reversed(marked)):
    if bit == "0": qc.x(q)
qc.h([0, 1]); qc.x([0, 1])
qc.h(1); qc.cx(0, 1); qc.h(1)
qc.x([0, 1]); qc.h([0, 1])
print(Statevector(qc).probabilities_dict())

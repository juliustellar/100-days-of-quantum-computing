from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

a = QuantumCircuit(1); a.h(0); a.x(0)
b = QuantumCircuit(1); b.x(0); b.h(0)
sa = Statevector.from_instruction(a)
sb = Statevector.from_instruction(b)
print(sa.equiv(sb))

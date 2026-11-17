from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.x(0)
qc.h(0)
qc.z(0)
state = Statevector.from_instruction(qc)
print(state.data)
print(state.probabilities_dict())

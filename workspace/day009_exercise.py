from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.ry(1.2, 0)
state = Statevector.from_instruction(qc)
print(qc.draw(output="text"))
print(state.probabilities_dict())

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import Statevector

theta = Parameter("theta")
qc = QuantumCircuit(1)
qc.ry(theta, 0)
bound = qc.assign_parameters({theta: 1.2})
print(Statevector(bound).probabilities_dict())

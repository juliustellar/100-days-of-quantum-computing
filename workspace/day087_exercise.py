from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, Statevector

qc = QuantumCircuit(2)
qc.ry(0.8, 0); qc.cx(0, 1)
hamiltonian = SparsePauliOp.from_list([
    ("ZI", -1.0), ("IZ", -1.0), ("XX", 0.5)])
state = Statevector.from_instruction(qc)
energy = state.expectation_value(hamiltonian)
print(float(energy.real))

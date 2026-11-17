from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def apply(gates):
    qc = QuantumCircuit(1)
    for name in gates:
        getattr(qc, name)(0)
    return Statevector(qc)

print(apply(["h", "s"]).data)

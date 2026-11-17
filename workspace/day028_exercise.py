from qiskit import QuantumCircuit

def measure_in_x(qc, qubit=0):
    qc.h(qubit)
    qc.measure(qubit, qubit)
    return qc

qc = QuantumCircuit(1, 1)
qc.h(0)
print(measure_in_x(qc))

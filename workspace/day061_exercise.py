from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 2)
qc.ry(0.7, 0)
qc.h(1); qc.cx(1, 2)
qc.cx(0, 1); qc.h(0)
qc.measure([0, 1], [0, 1])
with qc.if_test((qc.clbits[1], True)): qc.x(2)
with qc.if_test((qc.clbits[0], True)): qc.z(2)
print(qc)

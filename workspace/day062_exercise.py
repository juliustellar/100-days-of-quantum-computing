from qiskit import QuantumCircuit

bits = "10"
qc = QuantumCircuit(2, 2)
qc.h(0); qc.cx(0, 1)
if bits[1] == "1": qc.x(0)
if bits[0] == "1": qc.z(0)
qc.cx(0, 1); qc.h(0)
qc.measure([0, 1], [0, 1])
print(qc)

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

for theta in [0, pi/4, pi/2, 3*pi/4, pi]:
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    p1 = Statevector(qc).probabilities()[1]
    print(round(theta, 3), round(p1, 3))

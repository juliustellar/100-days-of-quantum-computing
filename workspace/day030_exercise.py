from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n = 4
qc = QuantumCircuit(n, n)
qc.h(range(n)); qc.measure(range(n), range(n))
sim = AerSimulator()
key = sim.run(transpile(qc, sim), shots=1).result()
bitstring = next(iter(key.get_counts()))
print(bitstring, int(bitstring, 2))

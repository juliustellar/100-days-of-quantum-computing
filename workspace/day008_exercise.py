from qiskit import QuantumCircuit

def prepare_basis(bitstring):
    qc = QuantumCircuit(len(bitstring))
    for qubit, bit in enumerate(reversed(bitstring)):
        if bit == "1":
            qc.x(qubit)
    return qc

print(prepare_basis("101"))

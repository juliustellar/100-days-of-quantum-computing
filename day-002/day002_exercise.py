from qiskit import QuantumCircuit

def build_circuit(gates):
    qc = QuantumCircuit(1)
    for gate in gates:
        getattr(qc, gate)(0)
    return qc

qc = build_circuit(["h", "z", "h"])
print(qc)

from qiskit import QuantumCircuit

def bell_block():
    block = QuantumCircuit(2, name="bell")
    block.h(0)
    block.cx(0, 1)
    return block.to_instruction()

qc = QuantumCircuit(2)
qc.append(bell_block(), [0, 1])
print(qc.decompose())

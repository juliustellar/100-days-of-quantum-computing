from qiskit import QuantumCircuit

prepare = QuantumCircuit(2); prepare.h(0)
logic = QuantumCircuit(2); logic.cx(0, 1)
measure = QuantumCircuit(2, 2)
measure.measure([0, 1], [0, 1])

qc = prepare.compose(logic).compose(measure)
print(qc)

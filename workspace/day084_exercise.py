from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.least_busy(
    operational=True, simulator=False)
print(backend.name)
print(backend.num_qubits)
print(sorted(backend.target.operation_names))

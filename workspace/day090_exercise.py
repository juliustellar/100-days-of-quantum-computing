from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1); qc.measure_all()
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
pm = generate_preset_pass_manager(backend=backend)
isa_qc = pm.run(qc)
job = SamplerV2(mode=backend).run([isa_qc], shots=1024)
print(job.job_id())

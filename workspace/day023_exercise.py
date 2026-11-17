from cmath import phase
from qiskit.quantum_info import Statevector

state = Statevector([1/2, (3**0.5)*1j/2])
for label, amp in zip(["0", "1"], state.data):
    probability = abs(amp) ** 2
    print(label, probability, phase(amp))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
print("Bell State Circuit:")print(qc.draw())

sim = AerSimulator()
job = sim.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("\nResults:")
for state, count in sorted(counts.items()):
    print(f"|{state}⟩: {count} times")

plot_histogram(counts)
plt.title("Quantum Entanglement - Bell State")
plt.show()

# Quantum Entanglement - Bell State Demo

Demonstrating quantum entanglement using a Bell state - where two qubits become perfectly correlated.

## 🔗 What Is This?

This project creates the simplest form of quantum entanglement. When you measure one qubit, you **instantly** know the state of the other - no matter how far apart they are. Einstein called this "spooky action at a distance."

## 🎯 The Magic

Running this code 1000 times produces:
- **|00⟩**: ~500 times (both qubits are 0)
- **|11⟩**: ~500 times (both qubits are 1)
- **|01⟩**: 0 times (never happens!)
- **|10⟩**: 0 times (never happens!)

The qubits are **perfectly correlated** - that's entanglement!

## 🔬 How It Works
```
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1
```

**Three steps:**
1. **H gate** on qubit 0 → Creates superposition
2. **CNOT gate** → Entangles qubit 1 with qubit 0
3. **Measure** → Both collapse together

## 💻 The Code (3 Key Lines)
```python
qc.h(0)              # Superposition
qc.cx(0, 1)          # Entanglement ← THE MAGIC
qc.measure([0,1], [0,1])  # Measure both
```

## 🚀 How to Run

### Install dependencies:
```bash
pip install qiskit qiskit-aer matplotlib
```

### Run:
```bash
python quantum_entanglement.py
```

## 📊 What You'll See

A histogram showing only |00⟩ and |11⟩ appearing - proof of entanglement!

![Results](quantum_entanglement_results.png)

## 🎓 What This Teaches

- **Superposition**: Qubits can be in multiple states at once
- **CNOT gate**: The tool for creating entanglement
- **Correlation**: Measuring one qubit determines the other
- **Bell state**: The foundation of quantum computing

## 🌟 Real-World Uses

- **Quantum Cryptography**: Unhackable communication
- **Quantum Teleportation**: Transfer quantum information
- **Quantum Computing**: Foundation of quantum algorithms
- **Quantum Sensing**: Ultra-precise measurements

## 📚 Learn More

- [Qiskit Textbook - Entanglement](https://qiskit.org/textbook/ch-gates/multiple-qubits-entangled-states.html)
- [Bell's Theorem](https://en.wikipedia.org/wiki/Bell%27s_theorem)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)

## 🛠️ Technologies

- Python 3.x
- Qiskit 1.x (IBM's quantum framework)
- Qiskit Aer (simulator)
- Matplotlib (visualization)

## 📝 Key Takeaway

Quantum entanglement is real, measurable, and the foundation of quantum computing's power. This simple demo proves it works!

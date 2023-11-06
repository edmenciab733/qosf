from qiskit import QuantumRegister
from qiskit import QuantumCircuit

c = QuantumRegister(1)
t = QuantumRegister(2)
a = c[:]+t[:]


qc = QuantumCircuit(a)
qc.draw()
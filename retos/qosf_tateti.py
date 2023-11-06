from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit.utils import algorithm_globals, QuantumInstance
import numpy as np

# Simulación de un juego de tic-tac-toe en un tablero de 3x3
b = [1, 2, 2, 1, 0, 0, 2, 0, 0]  # Estado actual del tablero


b = [1, 2, 2, 1, 0, 0, 0, 0, 0]  # Estado actual del tablero

# Inicializar el QuadraticProgram
qp = QuadraticProgram(name='Tic Tac Toe')

# Agregar variables binarias para cada posición vacía en el tablero
for i in range(9):
    if b[i] == 0:
        qp.binary_var(name=f'x{i}')


# Filas ganadoras
lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)]             # diagonals
    

for line in lines:
    for i in line:
        if b[i] == 0:
            qp.maximize(linear={f'x{i}': 1})
        

seed = 12345
algorithm_globals.random_seed = seed
backend = Aer.get_backend('aer_simulator')
quantum_instance = QuantumInstance(backend, seed_simulator=seed, seed_transpiler=seed)

# Ejecutar QAOA
qaoa = QAOA(reps=1, quantum_instance=quantum_instance)
optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qp)

# Interpretar y mostrar la solución
solution = result.variables_dict

print("Solución encontrada:", solution)

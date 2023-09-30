from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler


def find_the_primes_numbers(target, valores):
    # Crear un programa cuadrático
    qp = QuadraticProgram()

    # Añadir variables binarias para cada valor
    for i in range(len(valores)):
        qp.binary_var(f'x{i}')

    # Definir la función objetivo para maximizar la suma de los valores seleccionados
    linear_coef = {f'x{i}': valores[i] for i in range(len(valores))}
    qp.minimize(linear=linear_coef)
    qp.linear_constraint(linear=linear_coef, sense='EQ', rhs=target, name='sumatoria_restriccion')

    select_exactly_2 = {f'x{i}': 1 for i in range(len(valores))}
    qp.linear_constraint(linear=select_exactly_2, sense='EQ', rhs=2, name='select_exactly_3')


    # Crear una instancia de QAOA
    qaoa = QAOA(sampler=Sampler() ,optimizer=COBYLA())

    # Crear una instancia de MinimumEigenOptimizer utilizando QAOA
    optimizer = MinimumEigenOptimizer(min_eigen_solver=qaoa)

    # Resolver el problema de optimización
    result = optimizer.solve(qp)
    # Mostrar la solución
    return result.x, result.status.name, qaoa.ansatz

valores = [1,3,5,7,11,13,15, 17]
target = 28

x, resultado, circ = find_the_primes_numbers(target, valores)

print_cir = False
if print_cir:
    print(circ.draw())

print("La solución es: {}".format(resultado))


valores_seleccionados = [valores[i] for i, valor in enumerate(x) if valor == 1]

if(len(valores_seleccionados) > 0):
    print("La valores que cumplen la condición son: {}".format(valores_seleccionados))


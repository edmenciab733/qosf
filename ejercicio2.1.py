from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
def find_negative_numbers(valores):
    # Crear un programa cuadrático
    qp = QuadraticProgram()

    # Añadir variables binarias para cada valor
    for i in range(len(valores)):
        qp.binary_var(f'x{i}')

    # Definir la función objetivo para maximizar la suma de los valores seleccionados
    linear_coef = {f'x{i}': valores[i] for i in range(len(valores))}
    qp.maximize(linear=linear_coef)
    qp.linear_constraint(linear=linear_coef, sense='GE', rhs=1, name='sumatoria_restriccion')

    # Crear una instancia de QAOA
    qaoa = QAOA(sampler=Sampler() ,optimizer=COBYLA())

    # Crear una instancia de MinimumEigenOptimizer utilizando QAOA
    optimizer = MinimumEigenOptimizer(min_eigen_solver=qaoa)

    # Resolver el problema de optimización
    result = optimizer.solve(qp)
    # Mostrar la solución
    if result.status.name == "SUCCESS":
        return  True, qaoa.ansatz
    else:
         return  False, qaoa.ansatz


def calcular_bits(numeros):
    """Calcula el número de bits necesario para representar todos los números en la lista."""
    max_valor = max(abs(n) for n in numeros)
    bits = 0
    while max_valor:
        bits += 1
        max_valor >>= 1
    return bits + 1  # Añadir un bit adicional para el bit de signo

def a_complemento_a_dos(n, bits):
    """Convierte un número decimal a su representación en complemento a dos."""
    if n < 0:
        return bin((1 << bits) + n)[-bits:]  # Usar el slicing para asegurar la longitud correcta
    else:
        return bin(n)[2:].zfill(bits)


numeros = [-3, -7]
bits = calcular_bits(numeros)
binarios = [a_complemento_a_dos(n, bits) for n in numeros]
valores = [int(elemento[0])for elemento in binarios]
resultado, circ = find_negative_numbers(valores)

print(resultado)




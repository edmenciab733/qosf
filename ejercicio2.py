from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler

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


def de_complemento_a_dos(b, bits):
    """Convierte un número en complemento a dos a su representación decimal."""
    if b[0] == '1':
        return int(b, 2) - (1 << bits)
    else:
        return int(b, 2)


# Ejemplo de uso
numeros = [3, -7]
bits = calcular_bits(numeros)

binarios = []

binarios = [a_complemento_a_dos(n, bits) for n in numeros]

decimales = [de_complemento_a_dos(n, bits) for n in binarios]


#print(f"Nros originales: {numeros}")
#print(f"Representación en binarios ({bits} bits): {binarios}")
#print(f"Representación en decimales ({bits} bits): {decimales}")

#primeros_bits = [int(elemento[0])for elemento in binarios]
#print(f"Bits significativos {primeros_bits}")




from qiskit.visualization import plot_histogram
from qiskit_algorithms import Grover, AmplificationProblem
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.primitives import Sampler


def crear_oraculo(bits):
    # Crear un circuito cuántico con 2 qubits de entrada y 1 qubit auxiliar
    qc = QuantumCircuit(3)

    # Aplicar puertas X para invertir los qubits en 0

    qc.h(0)
    qc.h(1)
    qc.x(0)
    qc.x(1)
    

    # Aplicar una puerta CCX (Toffoli) que será activada si ambos qubits de entrada están en el estado |1>
    qc.ccx(0, 1, 2)

   

    return qc


primeros_bits = "11"
print(primeros_bits)
oraculo =crear_oraculo(primeros_bits)

def is_good_state(lista):
    return any(bit == 1 for bit in lista)

problem = AmplificationProblem(oracle=oraculo, is_good_state=is_good_state)
grover = Grover(sampler=Sampler())

result = grover.amplify(problem)
print( result.oracle_evaluation)

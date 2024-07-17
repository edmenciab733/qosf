import numpy as np
def separar_amplitudes(lista):
    num_q = int(np.log2(len(lista))) # saber a cuantos qubits corresponde su máxima longitud
    for i, amplitude in enumerate(lista):
        temp_b = format(i, "b") # convertir en binario el la posición del vector para poder 
        temp_b = temp_b.zfill(num_q) # rellenar con zeros a la izquierda
        print("{} |{}>".format(amplitude, temp_b)) # formatear el resultado


separar_amplitudes([0.7, 0.7, 0.7, 0])
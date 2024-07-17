import pennylane as qml
import numpy as np

nqubits = 4
dev = qml.device('default.qubit', wires=nqubits)
@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    qml.templates.AngleEmbedding(inputs, wires=range(nqubits))
    qml.templates.StronglyEntanglingLayers(weights, wires=range(nqubits))
    return qml.expval(qml.PauliZ(0))
    #return [qml.expval(qml.PauliZ(i)) for i in range(nqubits)]

num_layers = 4

shape = qml.StronglyEntanglingLayers.shape(n_layers=num_layers, n_wires=nqubits)

weights = np.random.random(shape)
X = np.array([[0, 0, 0, 0], [1, 1,1,1], [1, 0,0,0], [0, 0,0,0]])
Y = np.array([0, 1, 1, 0])


from sklearn.metrics import mean_squared_error
optimizer = qml.GradientDescentOptimizer(stepsize=0.4)

def cost(weights, X, y):
    predictions = [quantum_circuit(x, weights) for x in X]
    return mean_squared_error(y, predictions)


for it in range(100):
    weights = optimizer.step(lambda w: cost(w, X, Y), weights)
    if it % 10 == 0:
        print(f"Iteración {it}: Costo = {cost(weights, X, Y)}")

X = np.array([[0, 0, 0, 0], [1, 1,1,1], [1, 0,0,0], [0, 0,0,0]])
Y = np.array([0, 1, 1, 0])
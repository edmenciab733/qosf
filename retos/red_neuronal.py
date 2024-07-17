import numpy as np

# Funciones de activación y sus derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

# Función de pérdida de entropía cruzada y su derivada
def cross_entropy_loss(y_pred, y_true):
    return -np.sum(y_true * np.log(y_pred))

def cross_entropy_loss_derivative(y_pred, y_true):
    return y_pred - y_true

# Capa densa
class DenseLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size) * 0.01
        self.bias = np.zeros((output_size, 1))
        self.output = None
        self.input = None
        self.weight_gradient = None
        self.bias_gradient = None

    def forward(self, input):
        self.input = input
        self.output = np.dot(self.weights, input) + self.bias
        return self.output

    def backward(self, output_gradient):
        self.weight_gradient = np.dot(output_gradient, self.input.T)
        self.bias_gradient = output_gradient
        return np.dot(self.weights.T, output_gradient)

    def update(self, lr):
        self.weights -= lr * self.weight_gradient
        self.bias -= lr * self.bias_gradient

# Red Neuronal Simple
class SimpleNN:
    def __init__(self):
        self.layer1 = DenseLayer(4, 4)
        self.layer2 = DenseLayer(4, 3)

    def forward(self, input):
        x = sigmoid(self.layer1.forward(input))
        x = softmax(self.layer2.forward(x))
        return x

    def backward(self, y_pred, y_true):
        loss = cross_entropy_loss(y_pred, y_true)
        loss_gradient = cross_entropy_loss_derivative(y_pred, y_true)

        gradient = self.layer2.backward(loss_gradient)
        gradient = sigmoid_derivative(self.layer1.output) * gradient
        self.layer1.backward(gradient)

        return loss

    def update(self, lr):
        self.layer1.update(lr)
        self.layer2.update(lr)

# Crear una instancia del modelo
model = SimpleNN()

# ... [El resto del código permanece igual] ...

# Parámetros de entrenamiento
n_epochs = 10  # Número de epochs
learning_rate = 0.01

# Datos de entrenamiento
# Aquí necesitas tu conjunto de datos de entrada y las etiquetas correspondientes
# Por simplicidad, usaré datos aleatorios como ejemplo
inputs = [np.random.randn(4, 1) for _ in range(100)]  # 100 ejemplos aleatorios
labels = [np.random.randint(0, 3) for _ in range(100)]  # 100 etiquetas aleatorias
labels_one_hot = [np.eye(3)[label].reshape(3, 1) for label in labels]  # One-hot encoding

# Ciclo de entrenamiento
for epoch in range(n_epochs):
    total_loss = 0
    for input, label in zip(inputs, labels_one_hot):
        # Forward pass
        output = model.forward(input)

        # Backward pass y actualización
        loss = model.backward(output, label)
        model.update(learning_rate)

        total_loss += loss

    avg_loss = total_loss / len(inputs)
    print(f"Epoch {epoch + 1}, Loss: {avg_loss}")


print(f"Loss: {loss}")

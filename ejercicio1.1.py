import pulp

# Supongamos que esta es tu lista de salarios de los funcionarios
salarios = [800, 900, 700, 600, 1300, 1100, 750]

# Crea el problema de optimización
prob = pulp.LpProblem("Mejor_Combinacion", pulp.LpMaximize)

# Define las variables de decisión
# x_i será 1 si el funcionario i es seleccionado, 0 en caso contrario
x = [pulp.LpVariable(f'x{i}', cat='Binary') for i in range(len(salarios))]

# Define la restricción de la suma de salarios
prob += pulp.lpSum(x[i] * salarios[i] for i in range(len(salarios))) == 2000

# Define la restricción de seleccionar exactamente 2 funcionarios
prob += pulp.lpSum(x) == 2

# Resuelve el problema
prob.solve()

# Verifica si se encontró una solución
if pulp.LpStatus[prob.status] == 'Optimal':
    # Encuentra los funcionarios seleccionados
    seleccionados = [i for i in range(len(salarios)) if pulp.value(x[i]) == 1]
    print(f'Funcionarios seleccionados: {seleccionados}')
else:
    print('No se encontró una combinación de funcionarios que cumpla con las restricciones.')


lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]

b = [1, 2, 2, 1, 0, 0, 2, 0, 0]

def find_optimal_position(board, lines):
    # Revisar si podemos ganar en este movimiento.
    for line in lines:
        if sum(board[i] == 1 for i in line) == 2 and sum(board[i] == 0 for i in line) == 1:
            return line[next(i for i in range(3) if board[line[i]] == 0)]

    # Revisar si podemos bloquear al oponente de ganar en el siguiente movimiento.
    for line in lines:
        if sum(board[i] == 2 for i in line) == 2 and sum(board[i] == 0 for i in line) == 1:
            return line[next(i for i in range(3) if board[line[i]] == 0)]

    # Crear una doble oportunidad de ganar.
    for line in lines:
        if sum(board[i] == 1 for i in line) == 1 and sum(board[i] == 0 for i in line) == 2:
            # Comprobar si colocar aquí crea una doble oportunidad.
            potential_position = line[next(i for i in range(3) if board[line[i]] == 0)]
            board[potential_position] = 1  # Colocar temporalmente un '1' para la prueba.
            winning_opportunities = 0
            for check_line in lines:
                if sum(board[i] == 1 for i in check_line) == 3:
                    winning_opportunities += 1
            board[potential_position] = 0  # Remover el '1' después de la prueba.
            if winning_opportunities > 1:
                return potential_position

    # Preparar la victoria futura si no hay otra opción mejor.
    for line in lines:
        if sum(board[i] == 1 for i in line) == 1 and sum(board[i] == 0 for i in line) == 2:
            return line[next(i for i in range(3) if board[line[i]] == 0)]

    # Elección por defecto: el primer espacio vacío disponible.
    return next((i for i, x in enumerate(board) if x == 0), None)

optimal_position = find_optimal_position(b, lines)

if optimal_position is not None:
    print(f"La posición óptima para x=1 es: {optimal_position}")
    b[optimal_position] = 1
else:
    print("No hay posiciones óptimas disponibles.")

print("Estado actualizado de b:", b)

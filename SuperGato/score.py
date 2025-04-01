import numpy as np


def contar_tableros_diferencia(tablero, ficha) -> int:
    """
    tablero: Tablero
    jugador: int
    Devuelve la cantidad de subtableros en que el jugador tiene más fichas que el oponente
    """
    tableros_con_diferencia = 0
    for sub_tablero in tablero.tableros:
        contar_ficha_1 = 0
        contar_ficha_2 = 0
        for a in range(3):
            for i in range(3):
                if sub_tablero[a, i] == 1:
                    contar_ficha_1 += 1
                elif sub_tablero[a, i] == 2:
                    contar_ficha_2 += 1
        if ficha == 1 and contar_ficha_1 > contar_ficha_2:
            tableros_con_diferencia += 1
        elif ficha == 2 and contar_ficha_2 > contar_ficha_1:
            tableros_con_diferencia += 1
    return tableros_con_diferencia


def contar_fichas_seguidas(tablero, ficha) -> int:
    """
    tablero: Tablero
    ficha: int
    Devuelve la cantidad de pares de fichas seguidas de un jugador, se suma 3
    si tiene 3 seguidas (ganador del tablero)
    """
    puntos_mov = 0

    for subtablero in tablero.tableros:
        """"
        Aquí damos puntos por tablero ganado.
        Haremos algo similar a la función jugar de tablero, pero analizando
        subtablero por subtablero, ya que no tenemos los row ni col,
        y en cada uno tendremos que analizar fila por fila, columna y diagonal.
        Me basé en la función revisar_ganador de tablero para el código.
        """
        # Por columna
        for i in range(3):
            # revisaremos que los 3 espacios tengan el mismo símbolo y no sea vacío.
            if subtablero[i][0] == subtablero[i][1] == subtablero[i][2] and subtablero[i][0] != ' ':
                puntos_mov += 5

            # Por la fila
            if subtablero[0][i] == subtablero[1][i] == subtablero[2][i] and subtablero[0][i] != ' ':
                puntos_mov += 5

        # Por una diagonal
        if subtablero[0][0] == subtablero[1][1] == subtablero[2][2] and subtablero[0][0] != ' ':
            puntos_mov += 5

        # Por otra diagonal
        if subtablero[0][2] == subtablero[1][1] == subtablero[2][0] and subtablero[0][2] != ' ':
            puntos_mov += 5

    for subtablero in tablero.tableros:
        """
        vemos ahora si hay fichas una al lado de la otra en cada subtablero
        """

        # vemos los rows:
        for row in subtablero:
            for i in range(2):
                # veremos si una ficha es igual a otra que tenga a su lado derecho
                # y lo revisaremos con todas las fichas
                if row[i] == ficha and row[i] == row[i + 1]:
                    puntos_mov += 1

        # vemos columnas
        for j in range(3):
            for i in range(2):
                if subtablero[i][j] == ficha and subtablero[i][j] == subtablero[i + 1][j]:
                    puntos_mov += 1

    # vemos la primera diagonal
    for i in range(2):
        if subtablero[i][i] == ficha and subtablero[i][i] == subtablero[i + 1][i + 1]:
            puntos_mov += 1

    # vemos la otra
    for i in range(2):
        j = 2 - i
        if subtablero[i][j] == ficha and subtablero[i][j] == subtablero[i + 1][j - 1]:
            puntos_mov += 1

    if tablero.revisar_ganador() != 0:
        """
        Damos más puntaje por ganar el juego
        """
        puntos_mov += 15

    return puntos_mov


def contar_fichas_sin_enemigos(tablero, ficha) -> int:
    """
    Haremos algo similar a lo hecho en la función anterior, pero agregaremos
    que se sumarán puntos por fichas juntas solo si no hay una ficha enemiga
    en el mismo carril, de tal forma que sea posible ganar.
    """
    puntos_mov = 0

    for subtablero in tablero.tableros:
        """
        Conservamos el dar puntos por tablero ganado
        """
        # Por columna
        for i in range(3):
            if subtablero[i][0] == subtablero[i][1] == subtablero[i][2] and subtablero[i][0] != ' ':
                puntos_mov += 7

            # Por la fila
            if subtablero[0][i] == subtablero[1][i] == subtablero[2][i] and subtablero[0][i] != ' ':
                puntos_mov += 7

        # Por una diagonal
        if subtablero[0][0] == subtablero[1][1] == subtablero[2][2] and subtablero[0][0] != ' ':
            puntos_mov += 7

        # Por otra diagonal
        if subtablero[0][2] == subtablero[1][1] == subtablero[2][0] and subtablero[0][2] != ' ':
            puntos_mov += 7

    if ficha == "X":
        jugador = 1 # vamos a guardar el número de jugador para facilitar lo que sigue de código
    else:
        jugador = 2

    for subtablero in tablero.tableros:
        """
        Para esta parte me basé en la función jugar y en https://note.nkmk.me/en/python-numpy-count/
        Aquí sumamos el punto por tener al menos dos casillas en la misma fila y la otra libre
        """

        # vemos los rows:
        for row in subtablero:
            if np.count_nonzero(row == jugador) == 2 and 0 in row:
                puntos_mov += 2

        # vemos columnas
        for col in range(3):
            if np.count_nonzero(subtablero[:, col] == jugador) == 2 and 0 in subtablero[:, col]:
                puntos_mov += 2

    # vemos la primera diagonal
    diagonal1 = [subtablero[i][i] for i in range(3)]
    if np.count_nonzero(diagonal1 == jugador) == 2 and ' ' in diagonal1:
        puntos_mov += 2

    # vemos la otra
    diagonal2 = [subtablero[i][2 - i] for i in range(3)]
    if np.count_nonzero(diagonal2 == jugador) == 2 and ' ' in diagonal2:
        puntos_mov += 2


    if tablero.revisar_ganador() != 0:
        """
        Damos más puntaje por ganar el juego
        """

        puntos_mov += 30

    return puntos_mov

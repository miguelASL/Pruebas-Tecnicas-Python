"""Determinar si un  9 x 9tablero de Sudoku es válido. Sólo es necesario validar las celdas completadas  de acuerdo con las siguientes reglas :

Cada fila debe contener los dígitos  1-9sin repetición.
Cada columna debe contener los dígitos  1-9 sin repetición.
Cada uno de los nueve  3 x 3subcuadros de la grilla debe contener los dígitos  1-9 sin repetición.
Nota:

Un tablero de Sudoku (parcialmente lleno) podría ser válido pero no necesariamente tiene solución.
Sólo es necesario validar las celdas completadas de acuerdo con las reglas mencionadas.
 

Ejemplo 1:


Entrada: tablero =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Salida: verdadero
"""

#RESULTADO

class Solution(object):
    def isValidSudoku(self, board):
        # Función para verificar si una lista de números tiene duplicados
        def hasDuplicates(nums):
            seen = set()
            for num in nums:
                if num != '.':
                    if num in seen:
                        return True
                    seen.add(num)
            return False

        # Verificar filas y columnas
        for i in range(9):
            # Verificar fila
            if hasDuplicates(board[i]):
                return False

            # Verificar columna
            if hasDuplicates([board[j][i] for j in range(9)]):
                return False

        # Verificar subcuadros 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if hasDuplicates(subgrid):
                    return False

        return True

# Ejemplo de uso
sol = Solution()
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result = sol.isValidSudoku(sudoku_board)
print(result)  # Salida esperada: True

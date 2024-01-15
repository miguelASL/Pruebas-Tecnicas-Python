"""Dada una matriz de números enteros nums, gire la matriz hacia la derecha en kpasos, donde kno es negativo.

Ejemplo 1:

Entrada: números = [1,2,3,4,5,6,7], k = 3
 Salida: [5,6,7,1,2,3,4]
 Explicación:
rotar 1 paso a la derecha: [7,1,2,3,4,5,6]
rotar 2 pasos a la derecha: [6,7,1,2,3,4,5]
rotar 3 pasos a la derecha: [5,6,7,1,2,3,4]
"""

#RESULTADO
class Solution(object):
    def rotate(self, nums, k):
        # Si k es mayor que la longitud de la matriz, toma el módulo
        k = k % len(nums)
        
        # Gira la matriz hacia la derecha utilizando la técnica de slicing
        nums[:] = nums[-k:] + nums[:-k]
    # Ejemplo de uso
    numbers = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(numbers, k)
    print(numbers)  # Salida esperada: [5, 6, 7, 1, 2, 3, 4]
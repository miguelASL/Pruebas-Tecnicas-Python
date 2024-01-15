"""Dada una matriz de números enteros nums, mueva todos 0al final manteniendo el orden relativo de los elementos distintos de cero.
Tenga en cuenta que debe hacer esto in situ sin hacer una copia de la matriz.

Ejemplo 1:
Entrada: números = [0,1,0,3,12]
 Salida: [1,3,12,0,0]
 """
 
#RESULTADO

class Solution(object):
    def moveZeroes(self, nums):
        # Inicializar el puntero para la posición de los elementos no nulos
        non_zero_index = 0

        # Mover los elementos no nulos hacia la posición adecuada
        for i in range(len(nums)):
            if nums[i] != 0:
                # Si el elemento no es cero, muévelo a la posición adecuada
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Llenar el resto de la matriz con ceros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)

# Imprimir el resultado
print(nums)  # Salida esperada: [1, 3, 12, 0, 0]
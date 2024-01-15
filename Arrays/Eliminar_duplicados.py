"""Dada una matriz de enteros numsordenada en orden no decreciente , elimine los duplicados en el lugar de modo que cada elemento único aparezca solo una vez . El orden relativo de los elementos debe mantenerse igual . Luego devuelve el número de elementos únicos ennums .
Considere la cantidad de elementos únicos de numsto be k. Para ser aceptado, debe hacer lo siguiente:

Cambie la matriz numsde modo que los primeros kelementos numscontengan los elementos únicos en el orden en que estaban presentes numsinicialmente. Los elementos restantes de numsno son importantes al igual que el tamaño de nums.
Devolver k.

Entrada: nums = [1,1,2]
Salida: 2, nums = [1,2,_]
Explicación: Su función debería devolver k = 2, siendo los dos primeros elementos de nums 1 y 2 respectivamente. 
No importa lo que dejes más allá de la k devuelta (de ahí que sean guiones bajos).
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Inicializa el índice para los elementos únicos
        indice_unico = 0

        # Itera a través del arreglo empezando desde el segundo elemento
        for i in range(1, len(nums)):
            # Verifica si el elemento actual es diferente al anterior
            if nums[i] != nums[indice_unico]:
                # Incrementa el índice único
                indice_unico += 1
                # Mueve el elemento único a su posición correcta
                nums[indice_unico] = nums[i]

        # La cantidad de elementos únicos es (indice_unico + 1)
        return indice_unico + 1
    
# Ejemplo de uso
sol = Solution()
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
expectedNums = [1, 2, 3, 4, 5]

k = sol.removeDuplicates(nums)

# Verifica si el arreglo modificado coincide con la respuesta esperada
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

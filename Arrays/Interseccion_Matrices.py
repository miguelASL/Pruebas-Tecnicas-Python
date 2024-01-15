"""Dadas dos matrices de enteros nums1y nums2, devuelve una matriz de su intersección . Cada elemento del resultado debe aparecer tantas veces como se muestra en ambas matrices y puede devolver el resultado en cualquier orden .

Ejemplo 1:
Entrada: números1 = [1,2,2,1], números2 = [2,2]
 Salida: [2,2]
 """
 
 #Solucion
 
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        # Contar las frecuencias de los elementos en ambas matrices
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        
        # Inicializar una lista para almacenar la intersección
        intersection = []

        # Iterar sobre los elementos comunes a ambas matrices
        for num in count_nums1 & count_nums2:
            # Agregar el elemento repetido según la frecuencia común mínima
            intersection.extend([num] * min(count_nums1[num], count_nums2[num]))

        return intersection
    
sol = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = sol.intersect(nums1, nums2)
print(result)  # Salida esperada: [2, 2]
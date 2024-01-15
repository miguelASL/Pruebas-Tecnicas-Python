"""Dada una matriz de números enteros nums, devuelve truesi algún valor aparece al menos dos veces en la matriz y devuelve falsesi cada elemento es distinto.

Ejemplo 1:
Entrada: números = [1,2,3,1]
Salida: verdadero"""

# Resultado

class Solution(object):
    def containsDuplicate(self, nums):
        # Creamos un conjunto (set) para almacenar los elementos únicos que hemos encontrado
        seen = set()
        
        # Iteramos sobre la lista de números
        for num in nums:
            # Verificamos si el elemento ya está en el conjunto (ya ha sido encontrado antes)
            if num in seen:
                # Si encontramos un duplicado, devolvemos True
                return True
            
            # Agregamos el elemento al conjunto (ya que es la primera vez que lo encontramos)
            seen.add(num)
        
        # Si llegamos hasta aquí, no hemos encontrado duplicados, devolvemos False
        return False
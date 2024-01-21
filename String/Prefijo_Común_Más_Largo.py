"""Escriba una función para encontrar la cadena de prefijo común más larga entre una matriz de cadenas.
Si no hay un prefijo común, devuelve una cadena vacía "".

Ejemplo 1:
Entrada: strs = ["flor","flujo","vuelo"]
Salida: "fl
"""

# Respuesta

class Solution(object):
    def longestCommonPrefix(self, strs):
        # Si no hay cadenas en la lista, devuelve una cadena vacía
        if not strs:
            return ""
        
        # Ordena la lista de cadenas
        strs.sort()
        
        # La cadena más corta en la lista es el primer elemento
        # La cadena más larga en la lista es el último elemento
        # Estos dos elementos son los que más difieren
        first = strs[0]
        last = strs[-1]
        
        # Encuentra el prefijo común más largo entre la primera y la última cadena
        prefix = ""
        for i in range(len(first)):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        
        # Devuelve el prefijo común más largo
        return prefix
    
sol = Solution()

# Ejemplo 1: ["flower","flow","flight"]
# El prefijo común más largo es "fl"
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Debería imprimir "fl"

# Ejemplo 2: ["dog","racecar","car"]
# No hay un prefijo común, por lo que se devuelve una cadena vacía
print(sol.longestCommonPrefix(["dog","racecar","car"]))  # Debería imprimir ""

# Ejemplo 3: ["interspecies","interstellar","interstate"]
# El prefijo común más largo es "inters"
print(sol.longestCommonPrefix(["interspecies","interstellar","interstate"]))  # Debería imprimir "inters"
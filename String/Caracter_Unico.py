"""Dada una cadena s, busque el primer carácter no repetido que contenga y devuelva su índice . Si no existe, regresa -1.

Entrada: s = "aabb"
Salida: -1
"""

# Respuesta

class Solution(object):
    def firstUniqChar(self, s):
# Recorremos la cadena 's' utilizando índices
        for i in range(len(s)):
            # Verificamos si el carácter actual 's[i]' aparece solo una vez en la cadena
            if s.count(s[i]) == 1:
                # Si es así, devolvemos el índice actual como la primera posición única
                return i
        # Si no se encuentra ningún carácter único, devolvemos -1
        return -1

# Ejemplo de prueba
# Creamos una instancia de la clase Solution
sol = Solution()

# Probamos la función con una cadena de ejemplo
input_str = "leetcode"
result = sol.firstUniqChar(input_str)

# Imprimimos el resultado
print(f"La primera posición única en '{input_str}' es: {result}")
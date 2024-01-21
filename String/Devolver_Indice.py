"""Dadas dos cadenas needley haystack, devuelve el índice de la primera aparición de needleen haystack, o -1 si needleno forma parte de haystack.

Ejemplo 1:

Entrada: haystack = "sadbutsad", needle  = "sad"
 Salida: 0
 Explicación: "sad" ocurre en los índices 0 y 6.
La primera aparición está en el índice 0, por lo que devolvemos 0.
"""

# Respuesta

class Solution(object):
    def strStr(self, haystack, needle):
        # Si needle es una cadena vacía, devuelve 0
        if not needle:
            return 0
        
        # Si needle no está en el haystack, devuelve -1
        if needle not in haystack:
            return -1
        
        # Devuelve el índice de la primera aparición de la needle en el haystack
        return haystack.index(needle)


sol = Solution()
print(sol.strStr("sadbutsad", "sad"))  # Debería imprimir 0
print(sol.strStr("hello", "ll"))  # Debería imprimir 2
print(sol.strStr("aaaaa", "bba"))  # Debería imprimir -1
print(sol.strStr("", ""))  # Debería imprimir 0
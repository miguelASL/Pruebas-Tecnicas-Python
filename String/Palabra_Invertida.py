"""Escribe una función que invierta una cadena. La cadena de entrada se proporciona como una matriz de caracteres s.
Debe hacer esto modificando la matriz de entrada in situ con O(1)memoria adicional.

Ejemplo 1:
Entrada: s = ["h","e","l","l","o"]
 Salida: ["o","l","l","e","h"]
 """
 
 #RESULTADO
 
class Solution(object):
    def reverseString(self, s):
        return s.reverse()
    
# Uso de ejemplo:
cadena_original = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverseString(cadena_original)
print(cadena_original)
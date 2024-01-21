"""Dadas dos cadenas sy t, devuelve true si t es un anagrama de s, y false en caso contrario .
Un anagrama es una palabra o frase formada reorganizando las letras de una palabra o frase diferente, normalmente usando todas las letras originales exactamente una vez.

Ejemplo 1:
Entrada: s = "anagrama", t = "nagaram"
Salida: verdadero
 """
 
#Solucion
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
# Ejemplo de uso
sol = Solution()
s = "anagram"
t = "nagaram"
result = sol.isAnagram(s, t)
print(result)  # Expected output: True
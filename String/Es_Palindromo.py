"""Una frase es un palíndromo si, después de convertir todas las letras mayúsculas en minúsculas y eliminar todos los caracteres no alfanuméricos, se lee igual hacia adelante y hacia atrás. Los caracteres alfanuméricos incluyen letras y números.
Dada una cadena s, devuelve truesi es un palíndromo , o falseen caso contrario .

Ejemplo 1:
Entrada: s = "Un hombre, un plan, un canal: Panamá"
 Salida: verdadero
 Explicación: "amanaplanacanalpanama" es un palíndromo.

Ejemplo 2:
Entrada: s = "carrera de autos"
Salida: falso
Explicación: "carrera de autos" no es un palíndromo.

Ejemplo 3:
Entrada: s = " "
 Salida: verdadero
 Explicación: s es una cadena vacía "" después de eliminar caracteres no alfanuméricos.
Dado que una cadena vacía se lee igual hacia adelante y hacia atrás, es un palíndromo.
 
Restricciones:
1 <= s.length <= 2 * 105
sconsta únicamente de caracteres ASCII imprimibles."""

#RESULTADO

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s==s[::-1]
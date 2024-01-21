"""Implemente la myAtoi(string s)función, que convierte una cadena en un entero con signo de 32 bits (similar a la atoifunción de C/C++).

El algoritmo para myAtoi(string s)es el siguiente:

Lea e ignore cualquier espacio en blanco inicial.
Compruebe si el siguiente carácter (si no está al final de la cadena) es '-'o '+'. Lea este personaje si lo es. Esto determina si el resultado final es negativo o positivo respectivamente. Suponga que el resultado es positivo si ninguno de los dos está presente.
Lea a continuación los caracteres hasta llegar al siguiente carácter que no sea un dígito o al final de la entrada. El resto de la cadena se ignora.
Convierta estos dígitos en un número entero (es decir "123" -> 123, "0032" -> 32). Si no se leyeron dígitos, entonces el número entero es 0. Cambie el letrero según sea necesario (desde el paso 2).
Si el número entero está fuera del rango de enteros con signo de 32 bits , entonces fije el número entero para que permanezca en el rango. Específicamente, los números enteros menores que se deben fijar a , y los enteros mayores que se deben fijar a .[-231, 231 - 1]-231-231231 - 1231 - 1
Devuelve el número entero como resultado final.
Nota:

Sólo el carácter de espacio ' 'se considera un carácter de espacio en blanco.
No ignore ningún carácter que no sea el espacio en blanco inicial o el resto de la cadena después de los dígitos.
 

Ejemplo 1:

Entrada: s = "42"
 Salida: 42
 Explicación: Los caracteres subrayados son lo que se lee, el cursor es la posición actual del lector. 
Paso 1: "42" (no se leen caracteres porque no hay espacios en blanco al principio) 
         ^ 
Paso 2: "42" (no se leen caracteres porque no hay '-' ni '+') 
         ^ 
Paso 3: " 42 " (" Se lee 42") 
           ^ 
El número entero analizado es 42. 
Dado que 42 está en el rango [-2 31 , 2 31 - 1], el resultado final es 42."""

# Respuesta

class Solution(object):
    def myAtoi(self, s):
        # Elimina los espacios en blanco al principio y al final de la cadena
        s = s.strip()
        
        # Si la cadena está vacía, devuelve 0
        if not s:
            return 0
        
        # Asume que el número es positivo
        sign = 1
        
        # Si el primer carácter es un signo negativo, actualiza el signo y elimina el signo de la cadena
        if s[0] == '-':
            sign = -1
            s = s[1:]
        # Si el primer carácter es un signo positivo, simplemente elimina el signo de la cadena
        elif s[0] == '+':
            s = s[1:]
        
        # Inicializa el resultado como 0
        res = 0
        
        # Itera sobre los caracteres de la cadena
        for c in s:
            # Si el carácter es un dígito, lo añade al resultado
            if c.isdigit():
                res = res * 10 + int(c)
            # Si el carácter no es un dígito, termina el bucle
            else:
                break
        
        # Aplica el signo al resultado
        res = sign * res
        
        # Si el resultado es mayor que el máximo entero de 32 bits, devuelve el máximo entero de 32 bits
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        # Si el resultado es menor que el mínimo entero de 32 bits, devuelve el mínimo entero de 32 bits
        elif res < -2 ** 31:
            return -2 ** 31
        # Si no, devuelve el resultado
        else:
            return res
        
sol = Solution()
print(sol.myAtoi("-123"))  # Debería imprimir -123
print(sol.myAtoi("4193 with words"))  # Debería imprimir 4193
print(sol.myAtoi("words and 987"))  # Debería imprimir 0
print(sol.myAtoi("-91283472332"))  # Debería imprimir -2147483648 porque es menor que el mínimo entero de 32 bits
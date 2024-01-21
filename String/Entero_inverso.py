"""Dado un entero de 32 bits con signo x, regresa xcon sus dígitos invertidos . Si la inversión xhace que el valor salga del rango de enteros de 32 bits con signo , entonces devuelva .[-231, 231 - 1]0

Suponga que el entorno no le permite almacenar enteros de 64 bits (con o sin signo)
"""

# Solucion

class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Manejar el signo del número
        sign = 1 if x >= 0 else -1
        x *= sign

        # Invertir los dígitos
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # Verificar desbordamiento antes de multiplicar por 10
            if reversed_x > (INT_MAX - digit) // 10:
                return 0

            reversed_x = reversed_x * 10 + digit

        return reversed_x * sign
    
# Ejemplo de uso:
sol = Solution()
num = 123
result = sol.reverse(num)
print(result)
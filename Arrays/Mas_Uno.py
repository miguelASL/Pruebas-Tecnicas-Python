"""Se le proporciona un número entero grande representado como una matriz de números enteros digits, donde cada uno digits[i]es el dígito del número entero. Los dígitos están ordenados del más significativo al menos significativo de izquierda a derecha. El número entero grande no contiene ningún inicial .ith0
Incrementa el número entero grande en uno y devuelve la matriz de dígitos resultante .

Ejemplo 1:
Entrada: dígitos = [1,2,3]
 Salida: [1,2,4]
 Explicación: La matriz representa el número entero 123.
Incrementar en uno da 123 + 1 = 124.
Por tanto, el resultado debería ser [1,2,4].
"""

#RESULTADO

class Solution(object):
    def plusOne(self, digits):
# Inicializar el acarreo como 1 (para incrementar en uno)
        carry = 1

        # Iterar sobre los dígitos de derecha a izquierda
        for i in range(len(digits) - 1, -1, -1):
            # Sumar el dígito actual y el acarreo
            total = digits[i] + carry

            # Calcular el nuevo dígito y actualizar el acarreo
            digits[i] = total % 10
            carry = total // 10

        # Si queda un acarreo al final, agregarlo como un nuevo dígito
        if carry > 0:
            digits.insert(0, carry)

        return digits
sol = Solution()
digits = [1, 2, 3]
result = sol.plusOne(digits)
print(result)  # Salida esperada: [1, 2, 4]
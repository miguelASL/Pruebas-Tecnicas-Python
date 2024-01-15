"""Dada una  matriz de números enteros no vacíanums , cada elemento aparece dos veces excepto uno. Encuentra ese único.

Debe implementar una solución con una complejidad de tiempo de ejecución lineal y utilizar solo espacio adicional constante.
Entrada: números = [2,2,1]
Salida: 1 """

# Resultado

class Solution(object):
    def singleNumber(self, nums):
        resultado = 0
            
        for num in nums:
            resultado ^= num

        return resultado
    
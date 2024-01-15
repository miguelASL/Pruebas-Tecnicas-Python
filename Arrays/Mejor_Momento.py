"""Se le proporciona una matriz de números enteros pricesdonde prices[i]está el precio de una acción determinada en el
día.ith Cada día, usted puede decidir comprar y/o vender las acciones. Sólo puede poseer como máximo una acción a la
vez. Sin embargo, puedes comprarlo y venderlo inmediatamente el mismo día .
Encuentre y devuelva el máximo beneficio que pueda lograr .

Entrada: precios = [7,1,5,3,6,4]
 Salida: 7
 Explicación: Compre el día 2 (precio = 1) y venda el día 3 (precio = 5), ganancia = 5-1 = 4.
Luego compre el día 4 (precio = 3) y venda el día 5 (precio = 6), ganancia = 6-3 = 3.
La ganancia total es 4 + 3 = 7."""

#RESULTADO

class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0

        # Inicializar una lista para almacenar los beneficios hasta el día i
        profits = [0] * len(prices)

        # Iterar desde el segundo día hasta el final
        for i in range(1, len(prices)):
            # Calcular el beneficio si vendemos en el día i
            sell_today = prices[i] - prices[i-1] + profits[i-1]

            # Calcular el beneficio si no hacemos ninguna transacción en el día i
            no_transaction_today = max(profits[i-1], 0)

            # Actualizar el beneficio máximo hasta el día i
            profits[i] = max(sell_today, no_transaction_today)

        # El beneficio máximo estará en profits[-1]
        return profits[-1]
        # Ejemplo de uso
    prices = [7, 1, 5, 3, 6, 4]
    result = maxProfit(prices)
    print(result)  # Salida esperada: 7
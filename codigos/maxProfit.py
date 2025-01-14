# Usa o algoritmo do interval scheduling

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        return self._interval_scheduling_lucro_maximo(startTime, endTime, profit)

    def _interval_scheduling_lucro_maximo(self, inicio: List[int], fim: List[int], lucro: List[int]) -> int:
        # Combina os trabalhos em uma lista de tuplas e ordena por tempo de término
        trabalhos = sorted(zip(inicio, fim, lucro), key=lambda x: x[1])
        dp = [(0, 0)]  # (tempo de término, lucro máximo até agora)

        for inicio_atual, fim_atual, lucro_atual in trabalhos:
            # Busca binária para encontrar o último trabalho que não se sobrepõe
            indice = bisect_right(dp, (inicio_atual, float('inf'))) - 1
            lucro_incluindo = dp[indice][1] + lucro_atual
            # Atualiza o lucro máximo, incluindo ou excluindo o trabalho atual
            if lucro_incluindo > dp[-1][1]:
                dp.append((fim_atual, lucro_incluindo))

        return dp[-1][1]


def executar_casos_de_teste():
    casos_de_teste = [
        {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70],
            "esperado": 120
        },
        {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60],
            "esperado": 150
        },
        {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4],
            "esperado": 6
        },
    ]

    solucao = Solution()
    for i, caso in enumerate(casos_de_teste, start=1):
        resultado = solucao.jobScheduling(caso["startTime"], caso["endTime"], caso["profit"])
        if resultado == caso["esperado"]:
            print(f"Teste {i}: Passou ✅ (Esperado: {caso['esperado']}, Obtido: {resultado})")
        else:
            print(f"Teste {i}: Falhou ❌ (Esperado: {caso['esperado']}, Obtido: {resultado})")


# if __name__ == "__main__":
#     executar_casos_de_teste()
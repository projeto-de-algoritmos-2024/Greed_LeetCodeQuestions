# Usa o algoritmo do trocador

import heapq
from typing import List

class Solution:
    def minRefuelStops(self, destino: int, combustivel_inicial: int, postos: List[List[int]]) -> int:
        # Chama a lógica principal utilizando o algoritmo do trocador
        return self._algoritmo_trocador_paradas(destino, combustivel_inicial, postos)

    def _algoritmo_trocador_paradas(self, destino: int, combustivel_inicial: int, postos: List[List[int]]) -> int:
        # Adiciona o destino como um "posto de gasolina" com 0 combustível
        postos.append([destino, 0])
        max_heap = []  # Heap máxima para armazenar combustíveis disponíveis
        combustivel = combustivel_inicial
        paradas = 0
        posicao_anterior = 0

        for posicao, gasolina in postos:
            # Calcula o combustível restante após viajar até o próximo posto
            combustivel -= (posicao - posicao_anterior)

            # Enquanto não houver combustível suficiente, reabasteça
            while combustivel < 0 and max_heap:
                combustivel += -heapq.heappop(max_heap)  # Reabastece com o maior combustível disponível
                paradas += 1

            # Se não houver combustível suficiente e não puder reabastecer, retorne -1
            if combustivel < 0:
                return -1

            # Adiciona o combustível do posto atual à heap
            heapq.heappush(max_heap, -gasolina)
            posicao_anterior = posicao

        return paradas


def executar_casos_de_teste():
    casos_de_teste = [
        {"destino": 1, "combustivel_inicial": 1, "postos": [], "esperado": 0},
        {"destino": 100, "combustivel_inicial": 1, "postos": [[10, 100]], "esperado": -1},
        {"destino": 100, "combustivel_inicial": 10, "postos": [[10, 60], [20, 30], [30, 30], [60, 40]], "esperado": 2},
    ]

    solucao = Solution()
    for i, caso in enumerate(casos_de_teste, start=1):
        resultado = solucao.minRefuelStops(
            caso["destino"],
            caso["combustivel_inicial"],
            caso["postos"]
        )
        if resultado == caso["esperado"]:
            print(f"Teste {i}: Passou ✅ (Esperado: {caso['esperado']}, Obtido: {resultado})")
        else:
            print(f"Teste {i}: Falhou ❌ (Esperado: {caso['esperado']}, Obtido: {resultado})")


# if __name__ == "__main__":
#     executar_casos_de_teste()
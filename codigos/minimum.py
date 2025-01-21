from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Ordena os balões pelo ponto final
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for start, end in points:
            # Se o início do balão atual estiver fora do alcance da flecha atual
            if start > current_end:
                arrows += 1
                current_end = end
        
        return arrows


def executar_casos_de_teste():
    casos_de_teste = [
        {"points": [[10, 16], [2, 8], [1, 6], [7, 12]], "esperado": 2},
        {"points": [[1, 2], [3, 4], [5, 6], [7, 8]], "esperado": 4},
        {"points": [[1, 2], [2, 3], [3, 4], [4, 5]], "esperado": 2},
         {"points": [[1, 2]], "esperado": 1},
    ]

    solucao = Solution()
    for i, caso in enumerate(casos_de_teste, start=1):
        resultado = solucao.findMinArrowShots(caso["points"])
        if resultado == caso["esperado"]:
            print(f"Teste {i}: Passou ✅ (Esperado: {caso['esperado']}, Obtido: {resultado})")
        else:
            print(f"Teste {i}: Falhou ❌ (Esperado: {caso['esperado']}, Obtido: {resultado})")


if __name__ == "__main__":
    executar_casos_de_teste()

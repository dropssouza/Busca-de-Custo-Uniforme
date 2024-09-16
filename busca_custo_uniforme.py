#Busca de Custo Uniforme
#Pedro Henrique de Souza
#IA e Aprendizado de Máquina - Profº Drº Julio Tanomaru
#
#Pseudocódigo:
#Insere a cidade de origem na fila com custo 0 e o caminho de inicio
#Enquanto a fila não estiver vazia
#     Tira da fila o elemento com menor custo
#     Se a cidade fora da fila for o destino
#         Imprime o caminho e o custo
#         Sai do bloco
#     Caso contrário
#          Para cada vizinho da cidade fora da fila
#              Se a cidade vizinha não foi visitada
#                  Calcula o custo acumulado até a cidade vizinha
#                  Insere a cidade vizinha na fila com o custo acumulado e o caminho atualizado
#                  Marca a cidade vizinha como visitada
#Se a fila estiver vazia e o destino não foi encontrado
#    Imprime que não foi possível encontrar um caminho

import csv
from queue import PriorityQueue

def cria_grafo(caminho):
    mapa = {} #Dicionário vazio para armazenar o grafo
    with open(caminho, encoding='utf-8') as caminho_csv:
        arquivo_csv = csv.reader(caminho_csv, delimiter=',')
        cabecalho = 0
        for linha in arquivo_csv:
            if cabecalho == 0: #Verifica se está na primeira linha (cabeçalho), se estiver pula para a próxima
                cabecalho += 1
                continue
            #Se a cidade vizinha não estiver no dicionário mapa, adiciona como uma nova entrada
            if linha[0] not in mapa:
                mapa[linha[0]] = {}
            if linha[1] not in mapa:
                mapa[linha[1]] = {}

            #Adiciona o caminho no grafo a partir de um nó para o outro
            mapa[linha[0]][linha[1]] = int(linha[2])
            mapa[linha[1]][linha[0]] = int(linha[2])

    return mapa

def busca_custo_uniforme(grafo, origem, destino):
    fila_prioridade = PriorityQueue()
    cidades_visitadas = set()
    fila_prioridade.put((0, origem, [origem]))

    while not fila_prioridade.empty():
        cumulativo, cidade, caminho = fila_prioridade.get()

        fronteira = list(fila_prioridade.queue)
        print("\nBorda atual:", fronteira)
        print("Cidade escolhida da borda:", cidade)
        print("Custo da cidade escolhida:", cumulativo)
        print("Cidades já visitadas:", cidades_visitadas)

        #Marca a cidade como visitada
        if cidade in cidades_visitadas:
            continue
        cidades_visitadas.add(cidade)

        #Verifica se chegou ao destino
        if cidade == destino:
            print(f"\nCusto total: {cumulativo}")
            print(f"Rota encontrada: {caminho}")
            return caminho, cumulativo

        #Explora os vizinhos da cidade atual
        for proxima in grafo[cidade]:
            if proxima not in cidades_visitadas:
                custo_proxima = grafo[cidade][proxima]
                # Adiciona a cidade vizinha a fila com o custo acumulado atualizado e o caminho até ela
                fila_prioridade.put((cumulativo + custo_proxima, proxima, caminho + [proxima]))

    #Se a fila está vazia e não encontrou o destino, retorna que não foi possível encontrar o caminho
    print(f"Não foi possível encontrar um caminho de {origem} para {destino}.")
    return None, float('inf')

if __name__ == "__main__":
    caminho_arquivo = "cidades.csv"
    grafo = cria_grafo(caminho_arquivo)
    if grafo is not None:
        busca_custo_uniforme(grafo, "Marilia", "Bauru")

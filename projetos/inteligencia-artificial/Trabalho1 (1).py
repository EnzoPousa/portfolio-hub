from collections import deque

mapa = [
    ['S', '0', '1', '0', '0'],
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '0', '1'],
    ['0', '1', '1', '0', '0'],
    ['1', '0', '0', '0', 'G']
]

def busca_largura(mapa):

    # encontra S e G
    inicio = None
    objetivo = None

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'S':
                inicio = (i, j)
            if mapa[i][j] == 'G':
                objetivo = (i, j)

    # cria a fila
    fila = deque()
    fila.append(inicio)

    # cria o conjunto de visitados
    visitados = set()
    visitados.add(inicio)

    # cria uma estrutura para armazenar os caminhos
    caminhos = {}
    caminhos[inicio] = [inicio]

    # contador de posições exploradas
    exploradas = 0

    # enquanto houver posições na fila
    while len(fila) > 0:

        # retira uma posição da fila
        atual = fila.popleft()
        exploradas += 1

        # verifica se chegou ao objetivo
        if atual == objetivo:
            print("posições exploradas:", exploradas)
            return caminhos[atual]

        linha = atual[0]
        coluna = atual[1]

        # explora as quatro direções possiveis
        direcoes = [
            (-1, 0),  # cima
            (1, 0),   # baixo
            (0, -1),  # esquerda
            (0, 1)    # direita
        ]

        for direcao in direcoes:

            nova_linha = linha + direcao[0]
            nova_coluna = coluna + direcao[1]

            # adiciona os vizinhos validos a fila
            if nova_linha >= 0 and nova_linha < len(mapa):
                if nova_coluna >= 0 and nova_coluna < len(mapa[0]):

                    vizinho = (nova_linha, nova_coluna)

                    # verifica se não é parede e se ainda não foi visitado
                    if mapa[nova_linha][nova_coluna] != '1':
                        if vizinho not in visitados:

                            visitados.add(vizinho)
                            fila.append(vizinho)

                            caminhos[vizinho] = caminhos[atual] + [vizinho]

    print("não foi encontrado um caminho.")
    print("posições exploradas:", exploradas)

    return None


caminho = busca_largura(mapa)

print("caminho encontrado:", caminho)
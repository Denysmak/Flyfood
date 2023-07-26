def ler_matriz_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            num_linhas, num_colunas = map(int, arquivo.readline().strip().split())
            matriz = [['0' for _ in range(num_colunas)] for _ in range(num_linhas)]

            for linha_idx in range(num_linhas):
                elementos = arquivo.readline().strip().split()
                matriz[linha_idx] = elementos
        return matriz
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None

def encontrar_coordenadas_letras(matriz):
    coordenadas_letras = {}
    for linha_idx, linha in enumerate(matriz):
        for coluna_idx, elemento in enumerate(linha):
            if elemento == 'R':
                ponto_inicial = (linha_idx, coluna_idx)
            elif elemento not in ['R', '0']:
                coordenadas_letras[elemento] = (linha_idx, coluna_idx)
    return ponto_inicial, coordenadas_letras

def permutar(pontos_de_entrega):
    if len(pontos_de_entrega) <= 1:
        return [pontos_de_entrega]

    for i, ponto in enumerate(pontos_de_entrega):
        if ponto[0] == 'R':
            pontos_de_entrega[0], pontos_de_entrega[i] = pontos_de_entrega[i], pontos_de_entrega[0]
            break

    permutacoes = []
    for i, ponto_atual in enumerate(pontos_de_entrega):
        pontos_restantes = pontos_de_entrega[:i] + pontos_de_entrega[i+1:]
        for permutacao in permutar(pontos_restantes):
            permutacoes.append([ponto_atual] + permutacao)
    return permutacoes

def distancia(p1, p2):
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return dist

def dist_percurso(percurso):
    d = 0
    for i in range(1, len(percurso)):
        d += distancia(percurso[i - 1][1], percurso[i][1])

    d += distancia(percurso[-1][1], percurso[0][1])
    return d

# Teste a função com o arquivo exemplo matriz.txt
nome_arquivo = "matriz.txt"
matriz_lida = ler_matriz_arquivo(nome_arquivo)

if matriz_lida:
    ponto_inicial, coordenadas_letras = encontrar_coordenadas_letras(matriz_lida)
    coordenadas_rotulos = list(coordenadas_letras.items())
    coordenadas_rotulos.insert(0, ('R', ponto_inicial))

    menor = float("inf")
    menor_percurso = None
    for i in permutar(coordenadas_rotulos):
        dist = dist_percurso(i)
        if dist < menor:
            menor = dist
            menor_percurso = i

    menor_percurso_rotulos = [coord[0] for coord in menor_percurso]
    menor_percurso_rotulos.append('R')

    print(f"Menor percurso foi {menor_percurso_rotulos} com a distância de {menor} dronômetros")

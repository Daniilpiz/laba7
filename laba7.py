import random as rd
import numpy as np

import sys


def generator_smezh(razm):
    matr_sm = np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm)

    for i in range(razm):
        matr_sm[i, i] = 0
        for j in range(i):
            if i<=j:
                matr_sm[i, j] = matr_sm[j, i] if True else 0

    print(matr_sm)
    return matr_sm.tolist()


def search(G: list, visited: list, start: int, vyvod):
    visited[start] = True

    vyvod.append(start)
    print(f"Посетили узел: {start}")

    for i in range(len(G)):
        if G[start][i] == 1 and not visited[i]:
            search(G, visited, i, vyvod)

    return vyvod

def matrix_to_adj_list(matrix):
    """Функциональный стиль преобразования"""
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]

def matrix_to_adj_dict(matrix):
    n = len(matrix)
    graph = {}
    
    for i in range(n):
        graph[i] = {}  # инициализируем словарь для вершины i
        for j in range(n):
            weight = matrix[i][j]
            if weight != 0:  # ребро существует
                graph[i][j] = weight
    
    return graph



def search_2(adj_list: list, visited: list, start: int, vyvod):
    visited[start] = True
    vyvod.append(start)
    print(f"Посетили узел: {start}")

    # Проходим по всем соседям текущей вершины
    for neighbor in adj_list[start]:
        if not visited[neighbor]:
            search_2(adj_list, visited, neighbor, vyvod)

    return vyvod
            
            

sys.setrecursionlimit(10998)
def main():
    razm = int(input("Введите количество вершин:\t"))


    G = generator_smezh(razm)
    visited_1 = [0]*razm


    current = int(input("C какой вершины начать?\t"))

    lst_1 = []
    print(search(G, visited_1, current, lst_1))


    G = matrix_to_adj_dict(G)
    for vertex, neighbors in G.items():
        print(vertex, neighbors)


    current = int(input("C какой вершины начать?\t"))
    lst_2 = []
    visited_2 = [0]*razm

    
    print(search_2(G, visited_2, current, lst_2))

    

if __name__ == "__main__":
    main()
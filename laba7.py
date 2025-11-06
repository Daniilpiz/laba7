import random as rd
import numpy as np
import sys

import stack as st


def generator_smezh(razm):
    # Генерируем случайную матрицу смежности
    matr_sm = np.array([abs(rd.randint(0, 1000)) % 2 for _ in range(razm * razm)]).reshape(razm, razm)
    
    # Делаем матрицу симметричной (для неориентированного графа)
    for i in range(razm):
        matr_sm[i, i] = 0  # Нет петель
        for j in range(i + 1, razm):
            matr_sm[j, i] = matr_sm[i, j]  # Симметрируем
    
    print("Матрица смежности:")
    print(matr_sm)
    return matr_sm.tolist()


def dfs(G: list, visited: list, start: int, vyvod):
    visited[start] = True
    vyvod.append(start)
    print(f"Посетили узел: {start}")

    for i in range(len(G)):
        if G[start][i] == 1 and not visited[i]:
            dfs(G, visited, i, vyvod)

    return vyvod


def matrix_to_adj_list(matrix):
    """Функциональный стиль преобразования матрицы в список смежности"""
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]


def dfs_2(adj_list: list, visited: list, start: int, vyvod):
    visited[start] = True
    vyvod.append(start)
    print(f"Посетили узел: {start}")

    # Проходим по всем соседям текущей вершины
    for neighbor in adj_list[start]:
        if not visited[neighbor]:
            dfs_2(adj_list, visited, neighbor, vyvod)

    return vyvod

def dfs_non_recursion(G: list, visited: list, start: int, vyvod):
    stack = st.Stack()
    stack.push(start)
    visited[start] = True  # Помечаем стартовую вершину как посещенную сразу
    
    while not stack.is_empty():
        current = stack.pop()
        vyvod.append(current)
        print(f"Посетили узел: {current}")
        
        # Добавляем всех непосещенных соседей
        for i in range(len(G[current]) - 1, -1, -1):
            if G[current][i] == 1 and not visited[i]:
                visited[i] = True
                stack.push(i)
    
    return vyvod
 
def main():
    razm = int(input("Введите количество вершин:\t"))
    
    # Увеличиваем лимит рекурсии (осторожно!)
    sys.setrecursionlimit(max(10998, razm * 2))

    # Генерируем матрицу смежности
    matrix = generator_smezh(razm)
    visited_1 = [False] * razm

    current = int(input("C какой вершины начать?\t"))

    # Обход в глубину по матрице смежности
    print("\n--- DFS по матрице смежности ---")
    lst_1 = []
    print("Результат:", dfs(matrix, visited_1.copy(), current, lst_1))

    # Преобразуем в список смежности
    adj_list = matrix_to_adj_list(matrix)
    print("\n--- Список смежности ---")
    for vertex, neighbors in enumerate(adj_list):
        print(f"Вершина {vertex}: {neighbors}")

    # Обход в глубину по списку смежности
    print("\n--- DFS по списку смежности ---")
    current = int(input("C какой вершины начать?\t"))
    lst_1 = []
    visited_1 = [False] * razm
    print("Результат:", dfs_2(adj_list, visited_1, current, lst_1))

    # Нерекурсивный обход в глубину
    print("\n--- Нерекурсивный DFS ---")
    current = int(input("C какой вершины начать?\t"))
    lst_2 = []
    visited_1 = [False] * razm
    print("Результат:", dfs_non_recursion(matrix, visited_1.copy(), current, lst_2))


if __name__ == "__main__":
    main()
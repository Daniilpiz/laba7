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


    return matr_sm


def search(G: list, visited: list, start: int, vyvod):
    visited[start] = True

    vyvod.append(start)
    print(f"Посетили узел: {start}")

    for i in range(len(G)):
        if G[start][i] == 1 and not visited[i]:
            search(G, visited, i, vyvod)

    return vyvod
            
            

sys.setrecursionlimit(10998)
def main():
    razm = int(input("Введите количество вершин:\t"))

    visited = [0 for i in range(razm)]
    current = int(input("C какой вершины начать?\t"))
    lst = []
    print(search(generator_smezh(razm), visited, current, lst))



if __name__ == "__main__":
    main()
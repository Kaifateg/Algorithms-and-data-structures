import numpy as np


# Задача о рюкзаке
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n +1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = (max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]]) +
                            values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


weights = [1, 2, 3]
values = [50, 100, 130]
capacity = 6
print(knapsack(weights, values, capacity))


# Длина наибольшей общей подпоследовательности двух строк
def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


x = "AGSAFAFA"
y = "FFDSR"
print(lcs(x, y))


# Количество способов разбить число n на сумму чисел
def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


n = 4
print(count_partitions(n))


# Алгоритм Флойда-Уоршелла для нахождения кратчайших путей между всеми
# парами вершин в графе
def floyd_warshall(graph):
    n = len(graph)
    dist = np.array(graph, dtype=float)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = [
    [0, 3, 8, np.inf, -4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, -5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0]
]
print(floyd_warshall(graph))

import math
from random import random
from typing import List, Tuple

"""
랜덤하게 노드를 생성하고
"""

Coord = Tuple[int, int]
Matrix = List[List[bool]]
Cluster = List[List[int]]


def k_means(matrix: Matrix, k: int) -> Tuple[Cluster, List[Coord], int]:
    """
    k-means clustering algorithm
    1. 중심점을 k개 랜덤하게 생성한다.
    2. 다음 과정을 모든 중심점이 수렴할 때까지 반복한다.
    3. 각 데이터에 대해 중심점에서 가장 가까운 것을 계산 후 클러스터로 분류한다.
    4. 각 클러스터에 속한 데이터의 중심을 계산 후, 그 곳으로 클러스터의 중심점을 이동시킨다.
    """
    size = len(matrix)
    cluster = [[0] * size for _ in range(size)]

    cur_centroids = [(int(random() * size), int(random() * size)) for _ in range(k)]
    prev_centroids = []

    # 총 시행 횟수
    count = 0

    """
    중심점이 갱신되는 동안:
        Matrix의 각 노드에 대해:
            현재 노드와의 거리가 최소인 중심점을 찾아서, cluster 행렬을 갱신한다.
        각 클러스터에 포함한 원소들의 중앙값으로 중심점을 갱신한다.
    """
    while cur_centroids != prev_centroids:
        for i in range(size):
            for j in range(size):
                if matrix[i][j]:
                    dists = get_distances_to_node((i, j), cur_centroids)
                    cluster[i][j] = dists.index(min(dists)) + 1

        prev_centroids = cur_centroids[:]

        for K in range(k):
            count_k = 0
            acc_y = 0
            acc_x = 0

            for i in range(size):
                for j in range(size):
                    if cluster[i][j] == K + 1:
                        acc_y += i
                        acc_x += j
                        count_k += 1

            acc_y //= count_k
            acc_x //= count_k

            cur_centroids[K] = (acc_y, acc_x)

        count += 1

        print(f"----- {count}번째 시행 -----")
        _print_cluster(cluster)

    return cluster, cur_centroids, count


def init_matrix(size: int, points: int) -> Matrix:
    matrix = [[False] * size for _ in range(size)]

    for _ in range(points):
        y = int(random() * size)
        x = int(random() * size)

        matrix[y][x] = True

    return matrix


def get_distances_to_node(from_coord: Coord, nodes: List[Coord]) -> List[int]:
    dists: List[int] = []

    for node in nodes:
        dist = int(get_euclidean_distance(from_coord, node))
        dists.append(dist)

    return dists


def get_euclidean_distance(pq1: Coord, pq2: Coord):
    p1, q1 = pq1
    p2, q2 = pq2

    return math.sqrt((p1 - p2) ** 2 + (q1 - q2) ** 2)


def _print_matrix(matrix: Matrix) -> None:
    for row in matrix:
        for cell in row:
            print("O" if cell else ".", end=" ")
        print()
    print()


def _print_cluster(cluster: Cluster) -> None:
    clusters = ["★", "☆", "○", "●", "◎", "◇", "◆", "□", "■"]

    for row in cluster:
        for cell in row:
            print("." if cell == 0 else clusters[cell - 1], end=" ")
        print()
    print()


if __name__ == "__main__":
    size = int(input("행렬의 크기를 입력하세요(기본 20): ") or 20)
    points = int(input("노드의 개수를 입력하세요(기본 80): ") or 80)
    k = int(input("클러스터의 개수를 입력하세요(기본 3, 최대 9): ") or 3)

    matrix = init_matrix(size, points)
    print("초기 행렬:")
    _print_matrix(matrix)
    cluster, centroids, count = k_means(matrix, k)
    print(f"총 시행 횟수: {count}")

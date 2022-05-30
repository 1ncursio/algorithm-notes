import math


def get_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == "__main__":
    print(f"(1, 1)과 (4, 4)는 유클리드 거리 {get_euclidean_distance(1, 1, 4, 4)}만큼 떨어져 있음.")

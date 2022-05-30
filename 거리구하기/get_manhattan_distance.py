def get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    print(f"(1, 1)과 (4, 4)는 맨하탄 거리 {get_manhattan_distance(1, 1, 4, 4)}만큼 떨어져 있음.")

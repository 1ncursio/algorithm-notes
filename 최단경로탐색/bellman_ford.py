from typing import List, Tuple

Edge = Tuple[str, str, int]


def bellman_ford(edges: List[Edge], start: str):
    distance = [float("inf")] * (7 + 1)
    distance[start] = 0

    renewed = True
    while renewed:
        for edge in edges:
            u, v, w = edge

    return 1


if __name__ == "__main__":

    edges = []
    edges.append(("A", "B", 9))
    edges.append(("B", "A", 9))
    edges.append(("A", "C", 2))
    edges.append(("C", "A", 2))
    edges.append(("B", "C", 6))
    edges.append(("C", "B", 6))
    edges.append(("D", "C", 2))
    edges.append(("C", "D", 2))
    edges.append(("D", "B", 3))
    edges.append(("B", "D", 3))
    edges.append(("D", "E", 5))
    edges.append(("E", "D", 5))
    edges.append(("D", "F", 6))
    edges.append(("F", "D", 6))
    edges.append(("E", "F", 3))
    edges.append(("F", "E", 3))
    edges.append(("E", "G", 7))
    edges.append(("G", "E", 7))
    edges.append(("G", "F", 4))
    edges.append(("F", "G", 4))
    start = "A"
    bellman_ford(edges, start)
    print("ok")

from typing import List, TypeVar

T = TypeVar("T")


def rotate_matrix(matrix: List[List[T]]) -> List[List[T]]:
    """
    이차원 배열을 시계방향으로 90도 회전시킨다.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            (
                matrix[i][j],
                matrix[n - j - 1][i],
                matrix[n - i - 1][n - j - 1],
                matrix[j][n - i - 1],
            ) = (
                matrix[n - j - 1][i],
                matrix[n - i - 1][n - j - 1],
                matrix[j][n - i - 1],
                matrix[i][j],
            )

    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print(rotate_matrix(matrix))

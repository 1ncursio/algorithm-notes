
def selection_sort(array):
    for i in range(len(array)):
        min_index = i  # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스와프


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
            if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break


def quick_sort(array):
    """
    평균 시간 복잡도: O(NlogN)
    최악 시간 복잡도: O(N^2)
    """
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def count_sort(array):
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    """
    데이터가 양의 정수일 때 데이터의 개수를 N, 데이터 중 최댓값을 K라고 할 때
    시간 복잡도: O(N + K)
    공간 복잡도: O(N + K)
    """
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    selection_sort(array)
    print(array)

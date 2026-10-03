def binary_search(arr, target):
    """
    Бинарный поиск в отсортированном списке.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def linear_search(arr, target):
    """
    Линейный поиск. Нужен для сравнения.
    Возвращает индекс элемента или -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
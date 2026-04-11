def quick_sort(arr, low: int, high: int):
    """
    Task 2 Algorithm: Quick Sort O(n log n). Generic ones taught are O(n^2).
    Sort trades by date.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low: int, high: int) -> int:
    pivot = arr[high].date
    i = low - 1
    for j in range(low, high):
        if arr[j].date <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

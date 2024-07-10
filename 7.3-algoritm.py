def binary_search(list, target):
    low, high = 0, len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


list = [10, 22, 35, 47, 50, 62, 74, 85, 99]
target = 74
index = binary_search(list, target)
print(f"{target} elementi indexi: {index}")
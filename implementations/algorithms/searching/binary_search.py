from random import randint


def get_randomized_arr(size, _from=0, _to=100):
    ans = []
    while size > 0:
        ans.append(randint(_from, _to))
        size -= 1
    return ans


def binary_search(arr, value):
    # Return index of the value in the array
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < value:
            l = mid + 1
        elif arr[mid] > value:
            r = mid - 1
        else:
            return mid
    return -1


def binary_search_lower(arr, value):
    # Return index of first occurence, -1 otherwise
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= value:
            if arr[mid] == value:
                ans = mid
            l = mid + 1
        elif arr[mid] > value:
            r = mid - 1
    return ans


def binary_search_higher(arr, value):
    # Return index of last occurence, -1 otherwise
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < value:
            l = mid + 1
        elif arr[mid] >= value:
            if arr[mid] == value:
                ans = mid
            r = mid - 1
    return ans


arr = get_randomized_arr(20, 10, 15)
arr.sort()
print(arr)
print(binary_search(arr, 12))
print(binary_search_lower(arr, 12))
print(binary_search_higher(arr, 12))

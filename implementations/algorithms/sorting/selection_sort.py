from random import randint


def test_sort(size, sort):
    ans = []
    while size > 0:
        ans.append(randint(0, 200))
        size -= 1
    print('>>>', sort.__name__)
    print('Before:\t', ans)
    sort(ans)
    print('After:\t', ans)


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        key = i
        for j in range(i, n):
            if arr[key] > arr[j]:
                key = j
        arr[i], arr[key] = arr[key], arr[i]


test_sort(10, selection_sort)

# Idea: select the smallest element in the unsorted zone and put it at the front of the unsorted zone
# the worst

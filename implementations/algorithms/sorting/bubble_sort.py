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


def bubble_sort(arr):
    n = len(arr)
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                isSwapped = True

def bubble_sort_v1(arr):
    n = len(arr)
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                isSwapped = True
        n -= 1


test_sort(10, bubble_sort)
test_sort(10, bubble_sort_v1)

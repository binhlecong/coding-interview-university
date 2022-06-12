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


def counting_sort(arr, place):
    n = len(arr)
    count = [0] * 10
    for i in range(n):
        index = arr[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    output = [0] * n
    i = n - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    maxx = max(arr)
    place = 1
    while maxx // place > 0:
        counting_sort(arr, place)
        place *= 10


test_sort(10, radix_sort)

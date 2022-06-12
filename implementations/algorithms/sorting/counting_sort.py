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


def counting_sort(arr):
    m = max(arr)
    n = len(arr)
    count = [0] * (m + 1)
    for i in arr:
        count[i] += 1
    
    for i in range(1, m + 1):
        count[i] += count[i - 1]

    output = [0] * n
    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


test_sort(10, counting_sort)

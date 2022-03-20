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


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

test_sort(10, insertion_sort)

# best in O(n^2) algorithm
# perform better in small dataset 
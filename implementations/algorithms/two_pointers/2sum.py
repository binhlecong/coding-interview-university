# Given a sorted array A (sorted in ascending order), having N integers,
# find all pairs of elements (A[i], A[j]) such that their sum is equal to X.
arr = [10, 20, 35, 50, 60, 75, 80]


def findAllPair(a, x):
    a.sort()
    n = len(a)
    l, r = 0, n - 1
    ans = []
    while l < r:
        if a[l] + a[r] < x:
            l += 1
        elif a[l] + a[r] > x:
            r -= 1
        else:
            ans.append([a[l], a[r]])
            l += 1
    return ans


def findAllPair2(a, x):
    n = len(a)
    seen = set()
    ans = []
    for i in range(0, n):
        if (x - a[i]) in seen:
            ans.append([(x - a[i]), a[i]])
        else:
            seen.add(a[i])
    return ans


print(findAllPair2(arr, 70))
print(findAllPair(arr, 70))

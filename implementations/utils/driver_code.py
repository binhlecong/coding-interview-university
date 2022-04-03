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


def get_randomized_arr(size, _from=0, _to=100):
    ans = []
    while size > 0:
        ans.append(randint(_from, _to))
        size -= 1
    return ans

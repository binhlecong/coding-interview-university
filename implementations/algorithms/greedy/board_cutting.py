# https://www.hackerrank.com/challenges/board-cutting/problem
def boardCutting(cost_y, cost_x):
    cost = 0
    seg = [1, 1]
    y = sorted(cost_y, reverse=True)
    x = sorted(cost_x, reverse=True)
    for a in range(len(x)+len(y)):
        if len(x) is 0:
            cost += (seg[0]*y[0]) % (10**9+7)
            y.pop(0)
            seg[1] += 1
        elif len(y) is 0:
            cost += (seg[1]*x[0]) % (10**9+7)
            x.pop(0)
            seg[0] += 1
        else:
            if x[0] > y[0]:
                cost += (seg[1]*x[0]) % (10**9+7)
                x.pop(0)
                seg[0] += 1
            elif y[0] > x[0]:
                cost += (seg[0]*y[0]) % (10**9+7)
                y.pop(0)
                seg[1] += 1
            else:
                if seg[1] > seg[0]:
                    cost += (seg[0]*y[0]) % (10**9+7)
                    y.pop(0)
                    seg[1] += 1
                else:
                    cost += (seg[1]*x[0]) % (10**9+7)
                    x.pop(0)
                    seg[0] += 1

    return int(cost % (10**9+7))

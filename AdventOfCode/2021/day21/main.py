""" PART 2 """

import itertools

p1, p2 = 5, 10

dp = {}
def count_wins(p1, s1, p2, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    if (p1, s1, p2, s2) in dp:
        return dp[(p1, s1, p2, s2)]

    ans = (0, 0)
    for m1, m2, m3 in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        next_pos1 = (p1 + m1 + m2 + m3) % 10 if ((p1 + m1 + m2 + m3) % 10 != 0) else 10
        next_score1 = s1 + next_pos1
        x, y = count_wins(p2, s2, next_pos1, next_score1)
        ans = (ans[0]+y, ans[1]+x)
    dp[(p1, s1, p2, s2)] = ans
    return dp[(p1, s1, p2, s2)]

w1, w2 = count_wins(p1, 0, p2, 0)
print(w1, w2)
print(max(count_wins(p1, 0, p2, 0)))


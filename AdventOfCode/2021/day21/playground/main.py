""" PART 2 """

import itertools
import functools

@functools.lru_cache(maxsize=None)
def play_out(pos1, score1, pos2, score2):
    w1, w2 = 0, 0
    for m1, m2, m3 in itertools.product((1,2,3), (1,2,3), (1,2,3)):
        next_pos = (pos1 + m1 + m2 + m3) % 10 if ((pos1 + m1 + m2 + m3) % 10 != 0) else 10
        next_score = score1 + next_pos
        if next_score >= 21:
            w1 += 1
        else:
            w2_next, w1_next = play_out(pos2, score2, next_pos, next_score)
            w1 += w1_next
            w2 += w2_next
    return w1, w2


data = open('AdventOfCode/2021/day21/inputs/1.txt').read().strip().split('\n')
p1, p2 = int(data[0].split(': ')[1]), int(data[1].split(': ')[1])
print(p1, p2)
w1, w2 = play_out(p1, 0, p2, 0)
print(w1, w2)
print(max(w1, w2))

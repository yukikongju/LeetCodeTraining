# idea: always generate next price from smallest element

import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

prices = [0]
s = set()
for _ in range(K):
    smallest = heapq.heappop(prices)
    for a in A:
        new_price = smallest + a
        if new_price not in s:
            s.add(new_price)
            heapq.heappush(prices, new_price)

#  print(prices)
print(prices[0])

# sort sum of power set
# Edge cases:
# (1) duplicates of prices
# (2) prices not sorted
# (3) 

import heapq


N, K = map(int, input().split())
A = [int(a) for a in input().split()]
n = len(A)

A.sort()

i, j = 0, 0
prices = [0]
unique_prices = set(prices)

# 
while (len(prices) < K+1):
    x = prices[j] + A[i]
    if x not in unique_prices:
        unique_prices.add(x)
        prices.append(x)

    if (prices[j] + A[i] > prices[j+1] + A[0]) or (i==n-1):
        j+=1
        i=0
    else:
        i+=1

cmax = max(prices)

# add until combination has reached max
while((prices[j] + A[i]) < cmax):
    x = prices[j] + A[i]
    if x not in unique_prices:
        unique_prices.add(x)
        heapq.heappush(prices, x)

    if (prices[j] + A[i] > prices[j+1] + A[0]) or (i==n-1):
        j+=1
        i=0
    else:
        i+=1

prices.sort()


#  print(prices)
print(prices[K])




import heapq

#
N, Q = map(int, input().split())
called = []
came = [False]*(N+1)

#
idx1, idx3 = 1, 1
for i in range(Q):
    event = input().split()
    if event[0] == '1': # call for the first time
        heapq.heappush(called, idx1)
        #  print(f"{i} - First time: {idx}")
        idx1 += 1
    elif event[0] == '2': # comes
        p = int(event[1])
        came[p] = True
        if p == idx3:
            while (idx3 < N) and (came[idx3]):
                idx3 += 1
        #  print(f"{i} - has come: {p}")
    elif event[0] == '3':
        print(idx3)


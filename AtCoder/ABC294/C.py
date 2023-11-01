#
N, M = map(int, input().split())
A = list(map(int, input().split())) + [1e18]
B = list(map(int, input().split())) + [1e18]

#
A1 = [0]*N
B1 = [0]*M

i, j = 0, 0
while i<N or j<M:
    if (A[i] < B[j]):
        A1[i] = i+j+1
        i+=1
    else:
        B1[j] = i+j+1 
        j+=1

#
#  print(' '.join(map(str, A1)))
#  print(' '.join(map(str, B1)))
print(*A1)
print(*B1)


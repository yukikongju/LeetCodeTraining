

H, W = map(int, input().split())
S = [input() for _ in range(H)]

for s in S:
    t = list(s)
    for i in range(W-1):
        if (t[i] == 'T') and (t[i+1] == 'T'):
            t[i], t[i+1] = 'P', 'C'
    #          print(t)
    #  print()
    print(''.join(t))



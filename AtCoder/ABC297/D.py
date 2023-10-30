A, B = map(int, input().split())

# naive
#  t = 0
#  while (A != B):
#      if (A > B): A -= B
#      elif (A < B): B -=A
#      t += 1
#  print(t)

# using modulo
t = 0
while (A != B):
    if (A > B): 
        A -= (A//B)
        t += (A//B)
    elif (A < B): 
        B -= (B//A)
        t += (B//A)
print(t)

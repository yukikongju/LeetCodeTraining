# --- 1. read inputs
string = input()


# --- 2. counts => n1: y not a vowel ; n2: y is a vowel
n1, n2 = 0, 0
for s in string:
    if s in ['a', 'e', 'i', 'o', 'u']:
        n1 += 1
        n2 += 1
    if s == 'y': n2 += 1

print(n1, n2)

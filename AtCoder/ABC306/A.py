#  https://atcoder.jp/contests/abc306/tasks/abc306_a
# !python3 % < AtCoder/ABC306/inputs/a1.in;

# --- 1. read inputs
N = int(input())
S = input()

# --- 2. 
output = ''
for s in S:
    #  repeats = ord(s) - ord('a') + 1
    output += s*2

print(output)

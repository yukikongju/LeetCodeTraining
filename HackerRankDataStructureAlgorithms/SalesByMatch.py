#  https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#  There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# solution: count number of socks of each type and form the pair by suming 
# division


def sockMerchant(n, ar):
    # Write your code here
    socks = {}
    for sock in ar:
        socks[sock] = socks.get(sock, 0) + 1
    
    pairs = 0
    for key, value in socks.items():
        pairs += value // 2
    
    return pairs



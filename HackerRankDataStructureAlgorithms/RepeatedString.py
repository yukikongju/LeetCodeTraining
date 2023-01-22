#  https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#  There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first letters of the infinite string.


def repeatedString(s, n):
    # count the number of 'a' until the position in s
    occurences = [0]*len(s)
    for i, letter in enumerate(s): 
        has_a = 1 if letter == 'a' else 0
        occurences[i] = has_a + occurences[i-1] if i > 0 else has_a
    
    # 
    div, rest = divmod(n, len(s))
    return div * occurences[len(s)-1] + occurences[rest-1] if rest > 0 else div * occurences[len(s)-1]
    

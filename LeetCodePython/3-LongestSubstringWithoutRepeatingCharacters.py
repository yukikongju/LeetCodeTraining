#  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#  Given a string s, find the length of the longest substring without repeating characters.

# solution: add and remove letters from set whenever we increase/decrease 
# window size

def lengthOfLongestSubstring(self, s: str) -> int:
    # sliding window: use left and right pointer
    letters = set()
    longest = 0
    n = len(s)
    left, right = 0, 0

    while left < n and right < n:
        if s[right] not in letters:
            letters.add(s[right])
            right += 1
        else: 
            letters.remove(s[left])
            left += 1
        longest = max(longest, right - left)
    
    return longest
        


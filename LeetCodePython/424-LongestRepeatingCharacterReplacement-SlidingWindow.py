#  https://leetcode.com/problems/longest-repeating-character-replacement/description/
#  You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

#  Sol: 


def characterReplacement(self, s: str, k: int) -> int:
    letters = {}
    n = len(s)
    left, right = 0, 0
    longest = 0

    while left < n and right < n :
        # add letter to dict
        letters[s[right]] = 1 + letters.get(s[right], 0)
        
        # check if we need to increment/decrement window size
        # length of substring: right - left + 1
        while (right - left + 1) - max(letters.values()) > k:
            letters[s[left]] -= 1
            left += 1
        
        # update longest
        longest = max(longest, right - left + 1)

        right += 1

    
    return longest

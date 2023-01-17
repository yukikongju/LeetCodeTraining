#  https://leetcode.com/problems/group-anagrams/
# Neetcode:

def groupAnagrams(strs):
    # Sol 1: Sort every words and the words that are anagrams of each others will be mapped to 
    # the same words => O(m * n log n)
    # Sol 2: Create a Hashmap for each word where the key is the number of letter we see. 
    # The words that are mapped to the same key are groupped together => O(m*n*26)

    # create hashmap
    hashmap = {}
    for word in strs:
        key = [0]*26
        for letter in word: 
            idx_letter = ord(letter) - ord('a')
            key[idx_letter] += 1
        #  key = ''.join(map(str, key))
        key = tuple(key)
        if key not in hashmap: 
            hashmap[key] = [word]
        else:
            hashmap[key].append(word)

    return list(hashmap.values())

#  ---------------------------------------------------------------------------

def test1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    print(groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]])

def test2():
    strs = [""]
    print(groupAnagrams(strs))
    

def test3():
    strs = ["a"]
    print(groupAnagrams(strs))

def test4():
    strs = ["bdddddddddd","bbbbbbbbbbc"]
    print(groupAnagrams(strs))
    print("bbbbbbbbbbc" == "bbbbbbbbbbc")


def main():
    #  test1()
    #  test2()
    #  test3()
    test4()
    


if __name__ == "__main__":
    main()

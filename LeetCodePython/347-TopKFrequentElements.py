#  https://leetcode.com/problems/top-k-frequent-elements/
# NeetCode:

#  Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent1(nums, k):
    # Sol: Sort hashmap => O(n + n log n)

    # 1. make dictionary 
    count = {}
    for num in nums: 
        if num not in count:
            count[num] = 1
        else: 
            count[num] += 1

    # 2. sort dictionary
    order = [key for key, value in sorted(count.items(), key=lambda item: item[1], reverse = True)]

    return order[:k]

def topKFrequent2(nums, k):
    # Sol: count occurence of each number; create dict of each number counts; 
    # iterate to find last => O(n + )

    # 1. count the number of occurences => O(n)
    occurences = {}
    for num in nums: 
        occurences[num] = 1 + occurences.get(num, 0)
        #  if num not in occurences: 
        #      occurences[num] = 1
        #  else: 
        #      occurences[num] += 1

    # 2. create dict where each position correspond to the number of occurences
    count = [[] for _ in range(len(nums)+1)]
    for key, value in occurences.items():
        count[value].append(key)

    # 3. Find the k most frequent elements
    freq = []
    for i in range(len(count)-1, 0, -1):
        for num in count[i]: 
            freq.append(num)
            if len(freq) == k:
                return freq


def test1():
    nums = [1,1,1,2,2,3]
    k = 2

    print(topKFrequent2(nums, k))
    

def test2():
    nums = [1]
    k = 1

    print(topKFrequent2(nums, k))
    
def main():
    test1()
    test2()
    


if __name__ == "__main__":
    main()


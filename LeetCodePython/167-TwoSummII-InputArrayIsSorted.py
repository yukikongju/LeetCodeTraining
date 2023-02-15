#  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Sol: two pointers: start pointers at extremities. if sum left and right is 
# bigger than target, decrease right; if sum left and right smaller than 
# target, increase left. if pointer cross, impossible

def twoSum(numbers, target):
    left, right = 0, len(numbers) -1
    while left < right: 
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

    return -1


def test1():
    numbers = [2,7,11,15]
    target = 9
    #  print(twoSum(numbers, target))
    print(twoSum(numbers, target) == [1,2])


def main():
    test1()
    

if __name__ == "__main__":
    main()

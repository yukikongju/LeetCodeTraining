#  https://leetcode.com/problems/container-with-most-water/description/


def maxArea(height):
    left, right = 0, len(height) -1
    max_area = 0

    while left < right: 
        base = right - left
        min_height = min(height[left], height[right])
        area = base * min_height
        max_area = max(area, max_area)

        # check if we need to move left or right pointer
        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1

    return max_area

    


def test1():
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    print(maxArea(height) == 49)
    
def test2():
    height = [1,1]
    print(maxArea(height))
    print(maxArea(height) == 1)

def main():
    test1()
    test2()
    

if __name__ == "__main__":
    main()

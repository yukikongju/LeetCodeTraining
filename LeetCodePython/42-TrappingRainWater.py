#  https://leetcode.com/problems/trapping-rain-water/

#  Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


def trap(height):
    width = 1
    volume = 0

    if len(height) < 1: 
        return 0

    # 1. check if peak
    is_peak = [False]*len(height)
    for i in range(len(height)):
        if (i == 0 and height[i+1] <= height[i]):
            is_peak[i] = True
        elif i == len(height) -1 and height[i-1] <= height[i]:
            is_peak[i] = True
        else: 
            if height[i-1] <= height[i] and height[i+1] <= height[i]:
                is_peak[i] = True
    print(is_peak)




    # 2. get minimum peak height: iterate left/right

    # 3. calculate volume water trapped

    return volume
    
def test1():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height) == 6)
    
def test2():
    height = [4,2,0,3,2,5]
    print(trap(height) == 9)

def main():
    test1()
    test2()
    

if __name__ == "__main__":
    main()


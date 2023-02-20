class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # solution: O(nlogn)
        # - fastest we eat: largest value of the piles
        # - slowest we eat: sum(piles) // len(piles)
        # remark: we want the number of hours to take close to h, but it may not reach it

        # find k bound
        upper_bound = max(piles)
        lower_bound = 1
        k = upper_bound

        # find k 
        left, right = lower_bound, upper_bound + 1
        while left <= right:
            mid = (left + right) // 2
            hours = sum([ math.ceil(pile / mid) for pile in piles])
            if hours <= h: # we can decrease eating speed
                right = mid -1
                k = min(k, mid)
            elif hours > h: # we have to increase eating speed
                left = mid + 1
        print(left, right, mid)
        
        return k

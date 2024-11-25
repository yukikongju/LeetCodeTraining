#  https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    # solution: monotonic stack - non-increasing stack - O(n)

    def __init__(self):
        self.s = [] # (price, count)
        
    def next(self, price: int) -> int:
        if len(self.s) == 0:
            self.s.append((price, 1))
            return 1 
        
        count = 1
        while (len(self.s) > 0) and (self.s[-1][0] <= price):
            p, c = self.s.pop()
            count += c
        self.s.append((price, count))
        return count
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

class Solution:
    def minEatingSpeed(self, piles, h):
        l = 1 
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            tot=0
            for a in piles: 
                tot += ceil(a/ mid)
            if h < tot:
                l = mid + 1
            else: 
                r = mid
        return l

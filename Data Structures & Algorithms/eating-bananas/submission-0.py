class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        min_h = 0

        while s <= e:
            mid = (s+e) // 2

            if self.isPossible(mid, piles, h):
                min_h = mid
                e = mid - 1
            else:
                s = mid + 1

        return min_h
    
    def isPossible(self, k, piles, h):
        total_hour = 0
        for i in piles:
            total_hour += i // k
            total_hour += (0 if i % k == 0 else 1)

        return total_hour <= h

        
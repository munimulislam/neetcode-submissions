class Solution:
    arr = [None] * 45

    def climbStairs(self, n: int) -> int:     
        if n <= 1:
            return 1

        if not self.arr[n-1]:
            self.arr[n-1] = self.climbStairs(n-1)
        
        if not self.arr[n-2]:
            self.arr[n-2] = self.climbStairs(n-2)
        
        return self.arr[n-1] + self.arr[n-2]

        
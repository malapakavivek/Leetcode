class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        temp = 0
        for i in range(n - 1):
            temp = one + two
            one, two = temp, one
        return one
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1 / x, -n)
        elif n % 2 == 0:
            temp = self.myPow(x, n / 2)
            return temp * temp
        else:
            return x * self.myPow(x, n - 1)

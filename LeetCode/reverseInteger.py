class Solution:
    def reverse(self, x: int) -> int:
        reverseInt = int(str(abs(x))[::-1])
        if (x<0):
            reverseInt *= -1
        return reverseInt if -(2**31)-1 < reverseInt < 2**31 else 0
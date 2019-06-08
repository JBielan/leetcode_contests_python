class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            count += str(i).count(str(d))       # add to count how many times digit was in a number

        return count
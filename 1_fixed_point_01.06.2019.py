class Solution:
    def fixedPoint(self, A) -> int:
        for i in range(len(A)):     # go through the whole array
            if i == A[i]:       # if item equals to its index
                return i        # return index
        return -1       # otherwise return -1
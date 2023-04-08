class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        idx = 0
        for i in nums:
            idx += 1
            jdx = 0
            for j in nums:
                jdx += 1
                if (idx < jdx) and i == j:
                    good = good + 1
        return good

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        idx = -1

        for i in nums:
            idx += 1
            jdx = -1
            for j in nums:
                jdx += 1
                if (idx != jdx) and (i + j == k):
                    nums[idx] = 0.5
                    nums[jdx] = 0.9
                    pairs += 1
                    break

        return pairs

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        indexes = -1
        sorted_nums = sorted(nums)
        print(sorted_nums)
        for i in sorted_nums:
            indexes += 1
            if i == target:
                result.append(indexes)
        return result

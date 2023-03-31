class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def check(nums):
            for i in range(1, len(nums) - 1):
                if nums[i] == (nums[i-1] + nums[i+1]) / 2:
                    return True
            return False
        while check(nums):
            for i in range(1, len(nums) - 1):
                if nums[i] == (nums[i-1] + nums[i+1]) / 2:
                    swap(nums, i-1, i)
        return nums

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_int = []
        for i in range(len(nums)):
            nums_int.append(int(nums[i]))
        nums_int.sort()
        print(nums_int)
        return str(nums_int[-k])

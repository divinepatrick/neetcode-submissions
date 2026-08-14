class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        available = set()
        i = 0

        while i < len(nums):
            if nums[i] in available:
                return True
            available.add(nums[i])
            i += 1
        return False
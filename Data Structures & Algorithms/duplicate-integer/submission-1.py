class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i += 1
        return False
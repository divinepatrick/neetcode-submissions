class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            j = target - num
            if j in seen:
                return [seen[j] + 1, i + 1]
            seen[num] = i
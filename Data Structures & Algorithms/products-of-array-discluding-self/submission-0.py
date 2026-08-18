class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize output array with 1s
        output = [1] * n
        
        # First pass: left products
        # output[i] will store product of all elements to the left of i
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        # Second pass: Multiply with right products
        # Keep track of product of all elements to the right
        right_product = 1
        for i in range(n -1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        return output
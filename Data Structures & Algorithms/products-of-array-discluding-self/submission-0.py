class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Step 1: Compute prefix products directly in the output array
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Compute suffix products on the fly and multiply into output
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output

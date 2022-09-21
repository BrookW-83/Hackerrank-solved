class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        N = len(nums)
        
        
        res = 0
        
        for i in range (N):
                
                res = max (res, nums[i]+ nums[len(nums) - 1 -i])
                
        return res
                
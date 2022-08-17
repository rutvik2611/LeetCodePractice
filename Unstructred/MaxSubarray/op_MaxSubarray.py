nums = [-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    def maxSubArray(self, nums) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in range(len(nums)):
            
            if curSum < 0:
                curSum =0
            curSum += nums[n]
            maxSub = max(maxSub,curSum) 

        return maxSub

a = Solution()
print(a.maxSubArray(nums))
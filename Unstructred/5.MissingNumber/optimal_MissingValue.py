nums = [3,0,1]

class Solution:
    def missingNumber(self, nums) -> int:
        res =len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res

a =Solution()
print(a.missingNumber(nums))
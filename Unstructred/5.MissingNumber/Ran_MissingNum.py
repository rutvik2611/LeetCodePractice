nums = [3,0,1]

class Solution:
    def missingNumber(self, nums) -> int:
        maxx = max(nums)
        minx = min(nums)
        for i in range(minx,maxx):
            if i not in nums:
                return i
        return 0

a =Solution()
print(a.missingNumber(nums))
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    def rev(self,x):
        output = list(x)
        y,c ="",""
        for c in output:
            y = c + y
        return y

a = Solution()
nums = [1,2,3,4]
s = "skdjfjfkewjfkljeflwjeflleddddddd"
print(a.productExceptSelf(nums))
print(a.rev(s))
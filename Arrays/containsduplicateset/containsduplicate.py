class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set(nums)
        if len(x) == len(nums):
            return False
        else:
            return True
    def optcd(self,nums):
        h =set()
        for v in nums:
            if v in h:
                return True
            h.add(v)
        return False




a = Solution()
print(a.containsDuplicate([1,2,3,1]))
print(a.optcd([1,2,3,1]))
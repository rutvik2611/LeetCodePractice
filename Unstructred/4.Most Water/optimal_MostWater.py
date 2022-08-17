height= [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height) -> int:
        res =0
        l,r =0,len(height)-1
        while l<r:
            res = max(res,(r-l) * min(height[r],height[l]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return res

a =Solution()

print(a.maxArea(height))






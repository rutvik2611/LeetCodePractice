height= [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height) -> int:
        res =0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                

                #print(height[i]*height[j])
                res = max(res,(j-i) * min(height[i],height[j]))
        return res

a =Solution()

print(a.maxArea(height))
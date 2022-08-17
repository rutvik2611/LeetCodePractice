from typing import List, Any, Union

Input = [6, 5, 5]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > maxCount:
                maxCount = max(maxCount, count[i])
            # else:
            #     maxCount = res



        return maxCount


a = Solution()
print(a.majorityElement(Input))

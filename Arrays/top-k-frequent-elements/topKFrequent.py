import heapq
from typing import Counter


class Solution(object):
    def topKFrequent_old(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:

            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict.get(i)+1 #Sort by key and return top keys

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:

            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict.get(i)+1


        return heapq.nlargest(k,dict.keys(),key=dict.get)





a = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(a.topKFrequent(nums,k))
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Sudo Code
        '''
        1. Empty Dict and ret list of list
        2. Loop through the given array
        3. Sort every word in the array while looping and check if the sorted word in dict
        4. If not add it to dict with key(sorted) sorted val(orginal input) 
        5. If yes apped the (original value to sorted key)
        6. Loop through dict make list of list and return it
        '''
        dict = {}
        res = []
        for i in strs:
            s = "".join(sorted(i))
            if s not in dict:
                dict[s] = [i]
            else:
                dict[s].append(i)
        for item in dict.values():
            res.append(item)
        return res


a = Solution()
str = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(a.groupAnagrams(str))

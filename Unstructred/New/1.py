strs=["flower","flow","flight"]
def longestCommonPrefix(strs) -> str:
    res = "ef"
    for i in range(len(strs[0])):
        for s in strs:
            if i ==len(s) or s[i] != strs[0][i]:
                print(res)
                return res

    return res


print(longestCommonPrefix(strs))

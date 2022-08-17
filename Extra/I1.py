class Solution:
    def rev(self, x):
        output = list(x)
        y, c = "", ""
        for c in output:
            y = c + y
        return y

    def find_missing(self, Full, Par):
        for i in Full:
            if i in Par:
                pass
            else:
                return i
    def find_missing_XOR(self, Full, Par):
        xor_sum = 0
        for num in Full:
            xor_sum ^= num
        for num in Par:
            xor_sum ^= num
        return xor_sum


a = Solution()
s = "skdjfjfkewjfkljeflwjeflleddddddd"
print(a.rev(s))
Full = [4, 12, 6, 23]
Par = [4, 12, 23]
print(a.find_missing(Full, Par))
Full = [4, 12, 6, 23, 9]
Par = [4, 12, 23]
print(a.find_missing_XOR(Full, Par))

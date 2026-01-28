class Solution(object):
    def countAndSay(self, n):
        res = "1"

        for _ in range(n-1):
            cur = ""
            i = 0
            while i< len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                cur += str(count) + res[i]
                i += 1
            res = cur

        return res

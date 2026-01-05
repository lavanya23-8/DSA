class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        res = ""
        
        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res

class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2 = 1 
        prev1 = 1 
        
        for i in range(1, n):
            curr = 0
            
            if s[i] != '0':
                curr += prev1
            
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
            
            prev2 = prev1
            prev1 = curr
        
        return prev1
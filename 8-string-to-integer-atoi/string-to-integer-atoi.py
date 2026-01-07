class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            result = result * 10 +  int(s[i])
            if sign * result <= INT_MIN:
                return INT_MIN
            if sign * result >= INT_MAX:
                return INT_MAX


            i += 1

        return sign * result                   



        
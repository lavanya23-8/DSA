class Solution(object):
    def getPermutation(self, n, k):
        import math
        
        numbers = list(range(1, n + 1))
        k -= 1   
        result = ""
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            
            result += str(numbers[index])
            numbers.pop(index)
            
            k %= fact
        
        return result

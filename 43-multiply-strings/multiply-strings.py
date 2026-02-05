class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + res[pos2]
                
                res[pos2] = total % 10
                res[pos1] += total // 10
        
        # Convert to string, skipping leading zeros
        result = []
        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))
        
        return "".join(result) if result else "0"
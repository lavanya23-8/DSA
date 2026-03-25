class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, path):
            # If 4 parts formed
            if len(path) == 4:
                # If all digits used → valid IP
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Skip invalid cases
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res
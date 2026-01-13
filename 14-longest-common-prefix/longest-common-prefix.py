class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(len(prefix)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != prefix[i]:
                    return prefix[:i]

        return prefix

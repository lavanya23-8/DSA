class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in anagrams:
                anagrams[key] = []
            
            anagrams[key].append(word)
        
        return list(anagrams.values())

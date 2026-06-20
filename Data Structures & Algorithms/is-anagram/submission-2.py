class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashtable = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in hashtable:
                hashtable[char] = 1
            else:
                hashtable[char] += 1
        
        for char in t:
            if char not in hashtable:
                return False
            elif hashtable[char] != 0:
                hashtable[char] = hashtable[char] - 1
            elif hashtable[char] == 0:
                return False
            elif hashtable[char] < 0:
                return False
        
        return True
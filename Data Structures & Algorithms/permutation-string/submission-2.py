class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        hashtable = {}

        for char in s1:
            hashtable[char] = 1 + hashtable.get(char,0)
        
        j = 0
        for i in range(len(s2)):
            s2Hash = {}
            j = i
            while (j-i+1) <= len(s1) and j < len(s2):
                s2Hash[s2[j]] = 1 + s2Hash.get(s2[j],0)
                j += 1

            if s2Hash == hashtable: return True

        return False
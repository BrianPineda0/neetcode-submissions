class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ""

        if len(s) < len (t):
            return answer

        hashT = {}  

        hashS = {}
        
        for i in range(len(t)):
            hashT[t[i]] = 1 + hashT.get(t[i],0)
            hashS[t[i]] = hashS.get(t[i],0)
        

        need = len(t)
        have = 0
        best_len = float("inf")

        i = 0
        for j in range(len(s)):

            if s[j] not in hashT: continue

            if hashT[s[j]] > hashS[s[j]]:
                have += 1
                
            hashS[s[j]] = hashS.get(s[j]) + 1

            while need == have:

                if j - i + 1 < best_len:
                    best_len = j - i + 1
                    answer = s[i:j+1]

                if s[i] in hashS:
                    if hashS[s[i]] == hashT[s[i]]:
                        have -= 1
                    hashS[s[i]] = hashS.get(s[i]) - 1
                i += 1

        return answer
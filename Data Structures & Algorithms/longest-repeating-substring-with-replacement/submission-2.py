class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        hashtable = {}

        i = 0

        for r in range(len(s)):
            hashtable[s[r]] = 1 + hashtable.get(s[r],0)

            if (r - i + 1) - max(hashtable.values()) > k:
                hashtable[s[i]] -= 1
                i +=1
            
            answer = max(answer, (r - i + 1))    


        return answer
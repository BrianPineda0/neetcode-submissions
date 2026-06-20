class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setL = set()
        answer = 0
        i = 0

        for j in range(len(s)):
            while s[j] in setL:
                setL.remove(s[i])
                i +=1
            setL.add(s[j])
            answer = max(answer,len(setL))
        return answer
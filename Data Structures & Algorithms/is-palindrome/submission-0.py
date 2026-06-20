class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")

        cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
        
        for i in range(len(cleaned)):
            if cleaned[i] == cleaned[len(cleaned)-i-1]:
                continue
            else:
                return False

        return True
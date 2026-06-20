class Solution:

    def encode(self, strs: List[str]) -> str:

        parts = []

        for string in strs:
            parts.append(str(len(string)))
            parts.append("#")
            parts.append(string)
            

        word = "".join(parts)

        return word


    def decode(self, s: str) -> List[str]:

        answer = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            answer.append(s[j+1:j+1+length])

            i = j + 1 + length

        return answer

            
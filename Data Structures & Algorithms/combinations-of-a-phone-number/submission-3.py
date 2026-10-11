class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        hashTable = {}

        hashTable["2"] = ["a", "b", "c"]
        hashTable["3"] = ["d", "e", "f"]
        hashTable["4"] = ["g", "h", "i"]
        hashTable["5"] = ["j", "k", "l"]
        hashTable["6"] = ["m", "n", "o"]
        hashTable["7"] = ["p", "q", "r", "s"]
        hashTable["8"] = ["t", "u", "v"]
        hashTable["9"] = ["w", "x", "y", "z"]

        if digits == "":
            return []

        def dfs(i, curr):
            if len(curr) == len(digits) or i > len(digits):
                res.append("".join(curr))
                return
            
            for chars in hashTable[digits[i]]:
                curr.append("".join(chars))
                dfs(i+1, curr)
                curr.pop()

            return

        dfs(0, [])

        return res

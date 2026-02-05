class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        iterSize = -1
        lastLetter = s[iterSize]

        for letter in reversed(t):
            if lastLetter == letter:
                iterSize -= 1  

                if -iterSize > len(s):
                    return True

                lastLetter = s[iterSize]

        return False        
if __name__ == "__main__":
    print(Solution().isSubsequence("node", "neetcode")) 
        

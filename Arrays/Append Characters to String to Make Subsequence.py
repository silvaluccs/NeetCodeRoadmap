
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indexValue = 0

        lenT = len(t)   

        for letter in s:
            if indexValue < lenT and letter == t[indexValue]:
                indexValue += 1
        return  lenT - indexValue
        




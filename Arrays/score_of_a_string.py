class solution:
    def scoreofstring(self, s: str) -> int:
        sum_abs:int = 0
        for i in range(len(s) - 1):

            sum_abs += abs(ord(s[i+1]) - ord(s[i]))

        
        return sum_abs;



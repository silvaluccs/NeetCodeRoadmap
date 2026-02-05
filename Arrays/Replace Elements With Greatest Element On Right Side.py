from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sizeArr = len(arr)

        maxInArray = lambda a: max(a) if len(a) > 0 else -1

        for i in range(sizeArr):
            arr[i] = maxInArray(arr[i+1:])

        return arr
        

if __name__ == "__main__":
    print(Solution().replaceElements([2,4,5,3,1,2]))
        

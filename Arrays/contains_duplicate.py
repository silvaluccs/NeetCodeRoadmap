class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(dict(zip(nums, nums))) != len(nums)

if __name__ == "__main__":
    print(Solution().hasDuplicate([1, 2, 3, 3]))

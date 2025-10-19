class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                return [l + 1, r + 1]
            if summ > target:
                r -= 1
            else:
                l += 1
        raise Exception("Invalid Input!")
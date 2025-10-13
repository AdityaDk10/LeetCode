class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numset=set()
        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                return True

        return False
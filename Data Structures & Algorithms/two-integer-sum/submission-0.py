class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for index, num in enumerate(nums):
            diff = target - num
            if(diff in s):
                return [s.get(diff), index]
            s[num] = index

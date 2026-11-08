class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        
        for index , value in enumerate(nums):
            complement = target - value

            if complement in dict1:
                return [dict1[complement],index]

            dict1[value] = index    
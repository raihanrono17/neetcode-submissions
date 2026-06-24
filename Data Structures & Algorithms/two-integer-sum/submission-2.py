class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            for j in range(len(seen)+1,len(nums)):
                if nums[i] + nums[j] == target:
                    # return_list = [i,j]
                    return [i,j]
            seen.add(nums[i])

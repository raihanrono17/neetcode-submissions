class Solution:
    def sortColors(self, nums: List[int]) -> None:
        swap = True
        index = 0
        while swap == True and index < len(nums) -1:
            swap = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    swap = True
            index = index + 1
        
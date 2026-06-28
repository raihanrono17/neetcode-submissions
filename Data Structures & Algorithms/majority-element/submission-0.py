class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = []
        rec = []
        index = 0
        for i in range(len(nums)):
            if nums[i] not in majority:
                majority.append(nums[i])
                rec.append(0)
                for j in range(i,len(nums)):
                    if nums[j] == nums[i]:
                        rec[index] += 1 
                index += 1
        highest = rec[0]
        hi = 0
        for i in range(1,len(rec)):
            if rec[i] > highest:
                hi = i
        return majority[hi]
            
            

        
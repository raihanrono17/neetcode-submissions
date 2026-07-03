class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digit = {}
        for i in range(len(nums)):
            if nums[i] not in digit:
                digit[nums[i]] = 1
            else:
                digit[nums[i]] = digit[nums[i]] + 1
        x = sorted(digit, key=digit.get, reverse=True)
        returnlist = []
        for i in range(k):
            returnlist.append(x[i])
        return returnlist
        
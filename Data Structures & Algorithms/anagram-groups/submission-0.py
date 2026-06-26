class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        out = []
        for i in range(len(strs)):
            temp = []
            if "".join(sorted(strs[i])) in seen:
                    continue
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    temp.append(strs[j])
            temp.append(strs[i])
            seen.add("".join(sorted(strs[i])))
            out.append(temp)
        return out
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = set()
        for i in range(len(s)):
            counts = 0
            countt = 0
            if s[i] in seen:
                seen.add(s[i])
            else:    
                for j in range(len(s)):
                    if s[i] == s[j]:
                        counts += 1
                    if s[i] == t[j]:
                        countt += 1
                seen.add(s[i])
            if countt != counts:
                return False
        return True


test1: Solution = Solution().isAnagram("racecar","carrace")
        
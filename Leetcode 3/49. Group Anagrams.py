class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        result = []
        for i in strs:
            if str(sorted(i)) in s:
                s[str(sorted(i))].append(i)
            else:
                s[str(sorted(i))] = [i]
        for i in s:
            result.append(s[i])
        return result
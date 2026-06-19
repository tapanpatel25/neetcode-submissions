class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in pairs:
                pairs[key] = []
            pairs[key].append(i)

        return sorted(pairs.values())



        
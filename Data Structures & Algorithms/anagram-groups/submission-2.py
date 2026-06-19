
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        n = len(strs)
        for i in range(n):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(strs[i])
        # print(sorted_word)
    # print(d.items())
        return list(d.values())
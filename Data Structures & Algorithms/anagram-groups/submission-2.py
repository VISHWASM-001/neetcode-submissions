class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            if tuple(sorted(word)) in group:
                group[tuple(sorted(word))].append(word)
            else:
                group[tuple(sorted(word))] = [word]

        return list((group.values()))            
        
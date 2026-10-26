class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for char in strs:
            key= "".join(sorted(char))

            if key not in groups:
                groups[key] = []

            groups[key].append(char)

        return list(groups.values())


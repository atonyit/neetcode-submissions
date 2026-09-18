class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list) #if the list is empty edge case

        for word in strs:
            count = [0] * 26 #a - z
            for char in word:
                count[ord(char) - ord('a')] += 1
            mp[tuple(count)].append(word)

        return list(mp.values())
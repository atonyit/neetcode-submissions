class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSubstring, maxSubstring = set(), 0
        left, right = 0, 0

        while right < len(s):
            while s[right] in currSubstring:
                currSubstring.remove(s[left])
                left += 1

            currSubstring.add(s[right])
            maxSubstring = max(len(currSubstring), maxSubstring)
            right += 1


        return maxSubstring
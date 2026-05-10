class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #.sort() can only be used on arrays, not strings or tuples
        # sorted(x) is how we would do it for strings
        newS = sorted(s)
        newT = sorted(t)

        for i in range(len(newS)):
            if newS[i] != newT[i]:
                return False

        return True

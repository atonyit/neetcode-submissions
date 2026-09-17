class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        lowerS = s.lower()

        while i < j:
            if lowerS[i].isalnum() and lowerS[j].isalnum():
                if lowerS[i] != lowerS[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            elif not lowerS[i].isalnum():
                i += 1
            else:
                j-= 1
        return True

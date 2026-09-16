class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # new_s = sorted(s)
        # new_t = sorted(t)

        # return new_s == new_t

        s_mp = {}
        t_mp = {}

        for c in s:
            if c in s_mp:
                s_mp[c] += 1
            else:
                s_mp[c] = 1

        for c in t:
            if c in t_mp:
                t_mp[c] += 1
            else:
                t_mp[c] = 1

        return s_mp == t_mp

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mp = {}
        t_mp = {}
        
        #counters for both strings characters
        for c in s:
            s_mp[c] = s_mp.get(c, 0) + 1 #if c is not in hashmap, defualt value is 0 and then add 1 everytime to count
        
        for c in t:
            t_mp[c] = t_mp.get(c, 0) + 1 

        #now are the 2 hashmaps equal to each other, characters and frequency should match
        return s_mp == t_mp


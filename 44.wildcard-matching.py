#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    import itertools
    def isMatch(self, s: str, p: str) -> bool:
        si=0
        pi=0 
        stars=0 
        starp=-1
        
        slen=len(s)
        plen=len(p)
        
        while si<slen:
            if pi<plen and (p[pi]=="?" or p[pi]==s[si]): 
                si=si+1 
                pi=pi+1
            elif pi<plen and p[pi]=="*": 
                stars=si 
                starp=pi 
                pi=pi+1
            elif starp!=-1:
                stars=stars+1
                si=stars
                pi=starp+1
            else: 
                return False
        
        for _p in itertools.islice(p,pi,None):
            if _p!="*": 
                return False
                        
        return True
    
# @lc code=end


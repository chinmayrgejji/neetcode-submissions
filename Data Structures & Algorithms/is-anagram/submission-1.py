class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                if s[i] in seen :
                    seen[s[i]]+=1
                else:
                    seen[s[i]] = 1
                if t[i] in seen :
                    seen[t[i]]-=1
                else:
                    seen[t[i]]= -1
        return all(value==0 for value in seen.values())
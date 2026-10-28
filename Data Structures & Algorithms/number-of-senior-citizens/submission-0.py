class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for str in details :
            if int(str[11:13])>60:
                count+=1
        return count
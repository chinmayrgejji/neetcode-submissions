class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h=len(matrix)
        w=len(matrix[0])
        
        i=0
        j=0
        while i < h :
            if target in matrix[i]:
                return True 
            i+=1
            
        return False
            
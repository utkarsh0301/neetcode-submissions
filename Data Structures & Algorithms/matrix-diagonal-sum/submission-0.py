class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=(len(mat))
        for i in range(n):
            for j in range(len(mat[0])):
                
                if i == j or (i+j==n-1) :
                    sum+=mat[i][j]
        return sum 
        
        
        
        
    
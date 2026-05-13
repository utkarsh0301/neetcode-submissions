class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]==0):
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j]=0
        

                    
                    
        
       
     
        

        
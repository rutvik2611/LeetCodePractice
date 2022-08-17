matrix = [[1,1,1],[1,0,1],[1,1,1]]

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row ,col = len(matrix),len(matrix[0])
        rowZero = False

        #Findig zero rows

        for r in range(row):
            for c in range(col):

                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero =True

        #Writing in the matrix

        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c] == 0 and matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        if rowZero:
            for c in range(col):
                matrix[0][c]=0
        return matrix

        
a = Solution()

print(a.setZeroes(matrix))       
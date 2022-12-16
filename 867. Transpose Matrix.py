class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        matrix = [[1,2,3], [4,5,6], [7,8,9]]
        """
        res=[]
        for j in range(len(matrix[0])):
            acc=[]
            for i in range(len(matrix)):
                acc.append(matrix[i][j])
            res.append(acc)
        
        return res

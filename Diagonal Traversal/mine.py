class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        i, j = 0, 0
        result = []
        while i < m and j < n:
            result.append(mat[i][j])
            if (i+j) % 2 == 0:
                if j == n-1:
                    i += 1
                else:
                    if i > 0:
                        i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                else:
                    if j > 0:
                        j -= 1
                    i += 1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(a.findDiagonalOrder([[1, 2], [3, 4]]))
    print(a.findDiagonalOrder([[1, 2, 3, 4], [5, 6, 7, 8]]))

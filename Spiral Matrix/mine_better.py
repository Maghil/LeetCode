class Solution:
    def spiralOrder(self, mat):
        result = []
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        a = 1
        right, bot, left, top = True, False, False, False
        while len(result) < (m*n):
            result.append(mat[i][j])
            if right:
                if j < n - a:
                    j += 1
                else:
                    right, bot = False, True
            if bot:
                if i < m-a:
                    i += 1
                else:
                    bot, left = False, True
            if left:
                if j > a-1:
                    j -= 1
                else:
                    left, top = False, True
            if top:
                if i > a:
                    i -= 1
                else:
                    a += 1
                    j += 1
                    top, right = False, True
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8],
                         [9, 10, 11, 12], [13, 14, 15, 16]]))
    print(a.spiralOrder([[1, 2], [3, 4]]))
    print(a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

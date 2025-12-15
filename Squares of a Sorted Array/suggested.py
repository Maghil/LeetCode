import collections
class Solution:
    def sortedSquares(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)
    
if __name__ == "__main__":
    a = Solution()
    print(a.sortedSquares([-4, -1, 0, 3, 10]))
    print(a.sortedSquares([-7, -3, 2, 3, 11]))

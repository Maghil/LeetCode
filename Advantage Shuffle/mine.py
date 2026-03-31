class Solution:
    def advantageCount(self, a, b):
        n = len(a)
        indexes = list(range(n))
        indexes.sort(key=lambda i: b[i], reverse=True)
        a.sort(reverse=True)
        it = 0
        rit = n-1
        res = [0]*n
        for index in indexes:
            if a[it] > b[index]:
                res[index] = a[it]
                it += 1
            else:
                res[index] = a[rit]
                rit -= 1
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.advantageCount([1, 2, 3, 4, 5], [3, 5, 4, 6, 2]))
    print(a.advantageCount([1, 4, 2, 1, 3], [2, 3, 1, 2, 2]))
    print(a.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
    print(a.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))

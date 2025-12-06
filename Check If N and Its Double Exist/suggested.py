class Solution:
    def checkIfExist(self, arr) -> bool:
        seen = set()
        for i in arr:
            if 2 * i in seen or i / 2 in seen:
                return True
            seen.add(i)
        return False

if __name__ == "__main__":
    a = Solution()
    print(a.checkIfExist([10, 2, 5, 3]))
    print(a.checkIfExist([7, 1, 14, 11]))
    print(a.checkIfExist([3, 1, 7, 11]))
    print(a.checkIfExist([0, 0]))
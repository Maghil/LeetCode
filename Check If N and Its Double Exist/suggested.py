class Solution:
    def checkIfExist(self, arr) -> bool:
        seen = set()
        for i in arr:
            if 2 * i in seen or i / 2 in seen:
                return True
            seen.add(i)
        return False

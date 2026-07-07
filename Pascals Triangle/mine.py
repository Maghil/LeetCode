class Solution:
    def generate(self, numRows):
        result = []
        prev_row = [1]
        for i in range(numRows):
            result.append(prev_row)
            current_row = []
            for j in range(len(prev_row)+1):
                if j == 0:
                    current_row.append(1)
                if j == len(prev_row):
                    current_row.append(1)
                if (j != 0) and (j != len(prev_row)):
                    current_row.append(prev_row[j-1] + prev_row[j])
            prev_row = current_row
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.generate(5))





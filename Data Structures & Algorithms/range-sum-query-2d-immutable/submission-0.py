class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0

        # Extra row and column to avoid boundary checks
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            row_sum = 0

            for c in range(cols):
                row_sum += matrix[r][c]

                self.prefix[r + 1][c + 1] = (
                    row_sum
                    + self.prefix[r][c + 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Bottom-right
        br = self.prefix[row2 + 1][col2 + 1]

        # Area above
        above = self.prefix[row1][col2 + 1]

        # Area left
        left = self.prefix[row2 + 1][col1]

        # Top-left was subtracted twice, so add it back
        corner = self.prefix[row1][col1]

        return br - above - left + corner

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
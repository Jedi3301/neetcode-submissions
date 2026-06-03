class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in board[i][j+1:] or board[i][j] in board[i][:j]:
                        return False

        # Column check
        for j in range(9):
            for i in range(9):
                if board[i][j] != ".":
                    col = [board[r][j] for r in range(9)]
                    if col[i] in col[i+1:] or col[i] in col[:i]:
                        return False

        # Box check
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    box_row, box_col = (i // 3) * 3, (j // 3) * 3
                    box = [board[box_row + r][box_col + c] for r in range(3) for c in range(3)]
                    idx = (i % 3) * 3 + (j % 3)
                    if box[idx] in box[idx+1:] or box[idx] in box[:idx]:
                        return False

        return True  # only reaches here if all 3 checks pass
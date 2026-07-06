class Solution:
    # 3 arrays of sets here to track rows, column, and squares
    # classic 2D -> 1D trick: index = currentRow * numOfColumns+ currentColumn
    # adapt slightly for Sudoku because each big Square covers 9 little squares
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == '.':
                    continue
                box = (r // 3) * 3 + (c // 3)
                if (digit in rows[r] or
                digit in cols[c] or
                digit in boxes[box]):
                    return False
                else:
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)
        return True

                    

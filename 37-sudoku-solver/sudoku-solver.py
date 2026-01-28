class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(pos):
            if pos == len(empties):
                return True

            r, c = empties[pos]
            box_id = (r // 3) * 3 + c // 3

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    if backtrack(pos + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0)

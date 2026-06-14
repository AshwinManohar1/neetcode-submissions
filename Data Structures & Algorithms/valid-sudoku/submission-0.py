class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # each row 1-9 without duplicate
        # each column 1 -9 without duplicate
        # each sub boxes 3*3 without duplicate. 
        # can be empty. 

        n = len(board)
        
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)


                if val in columns[c]:
                    return False
                columns[c].add(val)

                box_idx = (r // 3 ) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)

            
        return True

                
                




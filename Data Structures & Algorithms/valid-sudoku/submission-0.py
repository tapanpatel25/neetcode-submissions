class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        is_valid = True

        # === 1. ROW CHECK ===
        for i in range(len(board)):
            seen = set()
            for j in board[i]:
                if j == '.':
                    continue
                
                if j not in seen:
                    seen.add(j)
                else:
                    print('wrong sudoku row')
                    is_valid = False
                    break
            if not is_valid:
                break
                
        if is_valid:
            print('exec column part')

            # === 2. COLUMN CHECK ===
            for col in range(9):
                seen = set()
                for row in range(9):
                    cell = board[row][col]
                    
                    if cell == '.':
                        continue
                    if cell not in seen:
                        seen.add(cell)
                    else:
                        print('wrong sudoku column')
                        is_valid = False
                        break
                if not is_valid:
                    break

        if is_valid:
            print('exec 3x3 part')

            # === 3. 3x3 GRID CHECK ===
            for row_block in range(0, 9, 3):
                for col_block in range(0, 9, 3):
                    seen = set()
                    
                    for r in range(3):
                        for c in range(3):
                            cell = board[row_block+r][col_block+c]
                            
                            if cell == '.':
                                continue
                            if cell in seen:
                                print('invalid 3x3')
                                is_valid = False
                                break
                            seen.add(cell)
                        if not is_valid: # Break out of 'r' loop
                            break
                    if not is_valid: # Break out of 'col_block' loop
                        break
                if not is_valid: # Break out of 'row_block' loop
                    break
        
        if not is_valid:
            return False
        else:
            return True
        
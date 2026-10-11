class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # only validate what is currently on the board
        # group by columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # group by row
        # only need to check duplicates -> compare sets
        # int length <-> set length
            # if different -> invalid
            # if same -> continue
        for row in board:
            seen = set()
            for item in row:
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen.add(item)
        # group by square
        # s1 s2 s3
        # s4 s5 s6
        # s7 s8 s9

        # shortcut - rangecuts
        for r in range(0, 9, 3): # -> (0, 3, 6)
            for c in range(0, 9, 3): # -> (0, 3, 6)
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True

        # # s1
        # seen = set()
        # for i in range(3):
        #     for j in range(3):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # # s2
        # seen = set()
        # for i in range(3):
        #     for j in range(3,6):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s3
        # seen = set()
        # for i in range(3):
        #     for j in range(6,9):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s4
        # seen = set()
        # for i in range(3,6):
        #     for j in range(3):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s5
        # seen = set()
        # for i in range(3,6):
        #     for j in range(3,6):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s6
        # seen = set()
        # for i in range(3,6):
        #     for j in range(6,9):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s7
        # seen = set()
        # for i in range(6,9):
        #     for j in range(3):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s8
        # seen = set()
        # for i in range(6,9):
        #     for j in range(3,6):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # #s9
        # seen = set()
        # for i in range(6,9):
        #     for j in range(6,9):
        #         num = board[i][j]
        #         if num == ".":
        #             continue
        #         if num in seen:
        #             return False
        #         seen.add(num)
        # return True


class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * (self.SIZE*self.SIZE))      #['.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):
        # 풀이
        for i, v in enumerate(self.board):
            print(v+' ', end='')
            if i % 3 == 2:
                print()

    def set(self, row, col):
        self.board[3*(row-1)+(col-1)] = self.turn

    def position_to_index(self, row,col):
        return 3*(row-1)+(col-1)

    def set_winner(self):
        # 파이썬 문제 풀이 ----------------
        # 가로 세로
        for row in range(1,3+1):
            if self.board[self.position_to_index(row,1)]\
            == self.board[self.position_to_index(row,2)]\
            == self.board[self.position_to_index(row,3)]\
            == self.turn :
                return self.turn
            if self.board[self.position_to_index(1,row)]\
            == self.board[self.position_to_index(2,row)]\
            == self.board[self.position_to_index(3,row)]\
            == self.turn :
                return self.turn

        # 대각선
        if self.board[self.position_to_index(1, 3)] \
        == self.board[self.position_to_index(2, 2)] \
        == self.board[self.position_to_index(3, 1)]\
        == self.turn:
            return self.turn
        if self.board[self.position_to_index(1, 1)] \
        == self.board[self.position_to_index(2, 2)] \
        == self.board[self.position_to_index(3, 3)]\
        == self.turn:
            return self.turn

        # , 더이상 놓을 자리가 없음: self.board에 빈칸이 없음: self.board에 '.' 없음
        if not '.' in self.board:
            return 'd'  # draw
        return ''

    def change_turn(self):
        self.turn = 'O' if self.turn=='X' else 'X'

class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)      #['.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):
        # 내가 짠 코드
        for i in range(len(self.board)):
            print((self.board[i]+"   ") if i%3!=2 else (self.board[i]+"\n"), end='')
        
        # 조별로 짠 코드
        for i in range(0,6+1,3):
            print('  '.join(self.board[i:i+3]))

        # 풀이
        for i, v in enumerate(self.board):
            print(v+' ', end='')
            if i % 3==2:
                print()
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
            == self.board[self.position_to_index(row,3)]:
                return '-'
            if self.board[self.position_to_index(1,row)]\
            == self.board[self.position_to_index(2,row)]\
            == self.board[self.position_to_index(3,row)]:
                return '|'

        # 대각선
        if self.board[self.position_to_index(1, 3)] \
        == self.board[self.position_to_index(2, 2)] \
        == self.board[self.position_to_index(3, 1)]:
            return '-'
        if self.board[self.position_to_index(1, 1)] \
        == self.board[self.position_to_index(2, 2)] \
        == self.board[self.position_to_index(3, 3)]:
            return '|'

        # 직접 짠 코드 ---------------------------------
        # - 3줄
        # for i in range(0, len(self.board), 3):
        #     if (self.board[i]==self.board[i+1]==self.board[i+2]):
        #         if(self.board[i]!='.'):
        #             print('-',self.board[i])
        # # | 3줄
        # for i in range(0,3):
        #     if (self.board[i]==self.board[i+3]==self.board[i+6]):
        #         if(self.board[i]!='.'):
        #             print('|',self.board[i])
        #
        # if self.board[2] == self.board[4] == self.board[6]:     # /
        #     return print(f'${self.board[2]} 승리')
        #
        # if self.board[0] == self.board[4] == self.board[8]:     # \
        #     return print(f'${self.board[0]} 승리')

        # 무승부: 위의 조건 다 통과   ------------------------
        for i in self.board:
            if i == '.':
                return '무승부 아님'
        # , 더이상 놓을 자리가 없음: self.board에 빈칸이 없음: self.board에 '.' 없음
        return 'd'  # draw

    def change_turn(self):
        self.turn = 'O' if self.turn=='X' else 'X'

if __name__ == '__main__':
    game_engin = TictactoeGameEngine()
    game_engin.show_board()     # ...\n...\n...
    game_engin.set(2,2)
    game_engin.show_board()     #['.','.','.','.','X','.','.','.']
    game_engin.set(2,1)
    game_engin.set(2,3)
    game_engin.show_board()     #['.','.','.','.'X','X','X','.','.']
    game_engin.set_winner()     # '-' 아무것도 안뜨게
    print(game_engin.turn)  # 'O'   현재 턴
    game_engin.change_turn()
    print(game_engin.turn)      # 'O'   현재 턴
    game_engin.change_turn()
    print(game_engin.turn)  # 'O'   현재 턴
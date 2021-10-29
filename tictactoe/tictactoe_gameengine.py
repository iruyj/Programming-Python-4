class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)      #['.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        pass

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
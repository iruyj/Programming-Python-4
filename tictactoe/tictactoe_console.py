from tictactoe.tictactoe_gameengine import TictactoeGameEngine


class TictactoeConsole:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        self.game_engine.show_board()
        # 무한반복
        while(True):
            # input row, col
            row = int(input('행 : '))
            col = int(input('열 : '))
            # set row, col
            self.game_engine.set(row,col)
            # show board
            self.game_engine.show_board()
            # set winner
            result = self.game_engine.set_winner()
            # 승자가 있거나 무승부면, 게임오버, 결과 출력
            if result == '': continue
            print('무승부' if result=='d' else f'승자 : {result}')


if __name__ == '__main__':
    tic = TictactoeConsole()
    tic.play()

# show_board
# input row, col
# set row, col
# show board
# set winner?
# 승자가 있으면 끝내고 출력
# change turn

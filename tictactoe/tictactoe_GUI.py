from tictactoe.tictactoe_console import TictactoeConsole


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeConsole()

    def init_GUI(self): # 화면구성 다때려넣기
        pass

    def click_handler(self, event):
        pass

if __name__ == '__main__':
    tic = TictactoeGUI()
import tkinter
from tkinter import messagebox      # 창띄워줌

from tictactoe.tictactoe_gameengine import TictactoeGameEngine


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self): # 화면구성 다때려넣기
        self.CANVAS_SIZE = 300      # 창크기 변수
        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False,height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white',width=self.CANVAS_SIZE,height=self.CANVAS_SIZE, cursor='hand2')
        self.canvas.pack()

        self.images = {}        # {'X' : PhotoImage 객체, 'O' : PhotoImage객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>',self.click_handler)
        # 함수() x -> 함수 : 함수가로를 치면안된다 ->순서가 맞지않아 바로 실행된다. ->버튼 클릭할때 실행할 함수의 이름만

        self.root.mainloop()

    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE // self.game_engine.SIZE
        x = 0
        y = 0

        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else:   # elif v == 'X' or v == 'O'
                # 이미지 화면에 그리기
                self.canvas.create_image(x,y, anchor = 'nw', image=self.images[v])
            x += TILE_SIZE

            if i % self.game_engine.SIZE == self.game_engine.SIZE -1:
                x=0;
                y+=TILE_SIZE

    def coordinate_to_position(self, x, y):
        return y//100+1, x//100+1    # 열, 행을 100으로 나누고 소수점 버림

    def click_handler(self, event):
        print(f'{event.x}, {event.y}')
        row, col = self.coordinate_to_position(event.x,event.y)
        print(row, col)
        # set row, col
        self.game_engine.set(row,col)
        # # show board
        self.game_engine.show_board()
        self.draw_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나 무승부면, 게임오버, 결과 표시하기
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner} 이김!!!🎉')
            self.root.destroy()
        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부!!!👯‍♀')
            print('무승부 입니다')
            self.root.destroy()
        self.game_engine.change_turn()

if __name__ == '__main__':
    tic = TictactoeGUI()
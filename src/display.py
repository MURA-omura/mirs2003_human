##
# @file display.py
# @author 村尾
# @date 2020/11/11


import tkinter as tk
from PIL import Image, ImageTk

##
# @brief ディスプレイ表示クラス
# @details タピ郎の走行状態に用いた画像をディスプレイに表示する。スレッド化して用いる。
class Display():
    ##
    # @brief ディスプレイの初期表示メソッド
    # @details 初期画像を読み込み、ウインドウを構築する。
    # @return None
    def start(self):
        self.img = None
        self.window = tk.Tk()
        self.window.title('タピ郎')
        self.window.attributes('-fullscreen', True)
        #self.window.state('zoomed')
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.img = Image.open('/home/pi/mirs/detect/image/sleep.png')
        self.img.thumbnail((self.width, self.height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.place(x=0, y=0)
        self.item = self.canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        self.window.mainloop()

    ##
    # @brief ディスプレイに表示する画像を変更するメソッド
    # @details タピ郎の状態が変化したときに新しい画像を読み込み、現在の画像と交換する。
    # @param state タピ郎の走行状態
    # @return None
    def changeImage(self, state: int):
        img_name = ['sleep.png', 'normal.png', 'normal.png', 'find.png', 'normal.png', 'onegai.png']
        self.img = Image.open('/home/pi/mirs/detect/image/' + img_name[state])
        self.img.thumbnail((self.width, self.height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.itemconfig(self.item, image=self.img)

    ##
    # @brief ウインドウの破棄メソッド
    # @details 特になし
    # @return None
    def quit(self):
        self.window.destroy()

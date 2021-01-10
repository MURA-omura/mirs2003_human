##
# @file interface.py
# @author 村尾
# @date 2020/11/11

from threading import Thread
from display import Display
from audio import Audio


##
# @fn main
# @brief メイン関数
# @return None
# @details ディスプレイをスレッド化し、タピ郎の状態をソケット通信で受け取って、状態変化時に指定の画像を表示して音をならす。
def main():
    dp = Display()
    ad = Audio()
    thread = Thread(target=dp.start)
    thread.setDaemon(True)
    thread.start()

    while True:
        if ad_flag > 0:
            ad.play(state)

if __name__ == '__main__':
    main()

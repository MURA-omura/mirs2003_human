##
# @file interface.py
# @author 村尾
# @date 2020/11/11


import sys
import threading
import time

from display import Display
from audio import Audio


##
# @fn main
# @brief メイン関数
# @return None
# @details ディスプレイをスレッド化し、タピ郎の状態をソケット通信で受け取って、状態変化時に指定の画像を表示して音をならす。
def main():
    detecter = Detection()
    dp = Display()
    ad = Audio()
    thread = threading.Thread(target=dp.start)
    thread.setDaemon(True)
    thread.start()

    for i in [j for j in range(10)]:
        print(i)
        if i == 5:
            dp.changeImage(1)
            ad.play(0)
        time.sleep(1)

    sys.exit()


if __name__ == '__main__':
    main()

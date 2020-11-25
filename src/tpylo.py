##
# @file interface.py
# @author 村尾
# @date 2020/11/11


import socket
from threading import Thread

from detection import Detection
from display import Display
from audio import Audio


##
# @fn main
# @brief メイン関数
# @return None
# @details ディスプレイをスレッド化し、タピ郎の状態をソケット通信で受け取って、状態変化時に指定の画像を表示して音をならす。
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 51000))

    detecter = Detection()
    dp = Display()
    ad = Audio()
    thread = Thread(target=dp.start)
    thread.setDaemon(True)
    thread.start()

    i = 0
    state_before = 0
    while True:
        i += 1
        motor_power = detecter.detect()

        # 走行プログラムと送信
        sock.sendall(b'{0}'.format(str(motor_power)))
        byte_data = sock.recv(8)
        state = int(byte_data.decode('utf-8'))

        if not state == state_before:
            dp.changeImage(state)
            ad.play(state)
        state = state_before

        if i > 100:
            break


if __name__ == '__main__':
    main()

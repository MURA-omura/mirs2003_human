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

    state_before = 0
    while True:
        motor_power, target_dist = detecter.detect()

        # 走行プログラムと送信
        sock.sendall(motor_power.to_bytes(2, 'big') + target_dist.to_bytes(2, 'big'))
        byte_data = sock.recv(4)
        #print(byte_data)
        state = int.from_bytes(byte_data[:2], 'big')
        ad_flag = int.from_bytes(byte_data[2:], 'big')

        #print(state)
        if state != state_before:
            dp.changeImage(state)
            if ad_flag == 1:
                if state_before == 0:
                    ad.play(0)
                elif state == 5:
                    ad.play(1)
                elif state_before == 5:
                    ad.play(2)
        state_before = state


if __name__ == '__main__':
    main()

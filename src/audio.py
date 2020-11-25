##
# @file audio.py
# @author 村尾
# @date 2020/11/11


import simpleaudio as sa


##
# @brief 音声再生クラス
# @details タピ郎の走行状態に用いた音声を再生する。
class Audio():
    ##
    # @brief コンストラクタ
    # @details 鳴らす音声の読み込みを行う。
    # @return None
    def __init__(self):
        self.wave = sa.WaveObject.from_wave_file('../audio/wave.wav')

    ##
    # @brief 再生関数
    # @details タピ郎の状態が変化したときに指定の音声を再生する。
    # @param state タピ郎の走行状態
    # @return None
    def play(self, state):
        pl = self.wave.play()
        #pl.wait_done()

##
# @file target.py
# @author 村尾
# @date 2020/11/21

##
# @brief 人検出クラス
# @details カメラからキャプチャをし、そこから人がいる領域にバウンディングボックスを描画する
class Target():
    ##
    # @brief コンストラクタ
    # @return None
    def __init__(self):
        pass

    ##
    # @brief ターゲット設定メソッド
    # @details 入力されたidに対応するラベルを返す
    # @param target_array 人のバウンディングボックスの中心点のx座標、横縦の大きさ
    # @return power 左右のタイヤのPWM調整値
    def setTarget(self, target_array):
        max_height = 0.0
        target_num = -1
        for i, target in enumerate(target_array):
            if target[1] > max_height:
                target_num = i
        if target_num >= 0:
            power = self.adjustMotor(target_array[target_num][0])
            return power
        else:
            return 0

    ##
    # @brief モータPWM値調整メソッド
    # @details ターゲットのバウンディングボックスの中央座標から左右のモータの調整値を導出する
    # @return power 左右のタイヤのPWM調整値
    def adjustMotor(self, posx):
        print(posx)
        rate = 30
        power = rate * (posx - 0.5)
        return power

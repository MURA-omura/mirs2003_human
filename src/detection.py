##
# @file detection.py
# @author 村尾
# @date 2020/11/11


import cv2
from target import Target


##
# @brief 人検出クラス
# @details カメラからキャプチャをし、そこから人がいる領域にバウンディングボックスを描画する
class Detection():
    classNames = {0: 'background',
                  1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
                  7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
                  13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
                  18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
                  24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
                  32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
                  37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
                  41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
                  46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
                  51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
                  56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
                  61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
                  67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
                  75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
                  80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
                  86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

    ##
    # @brief コンストラクタ
    # @details カメラをオープンする
    # @return None
    def __init__(self):
        self.model = cv2.dnn.readNetFromTensorflow('../model/ssd_mobilenet_v2.pb', '../model/ssd_mobilenet_v2.pbtxt')
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError('Cannot open camera')
        self.cap.set(cv2.CAP_PROP_FPS, 5)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
        _, image = self.cap.read()
        self.image_height, self.image_width, _ = image.shape
        self.target = Target()

    ##
    # @brief ラベル取得メソッド
    # @details 入力されたidに対応するラベルを返す
    # @param class_id ラベルID
    # @return value ラベル名
    def getName(self, class_id):
        for key, value in self.classNames.items():
            if class_id == key:
                return value

    ##
    # @brief 人検出メソッド
    # @details カメラからキャプチャし、人を検出する
    # @return None
    def detect(self):
        _, image= self.cap.read()
        self.model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
        output = self.model.forward()
        target_pos = []
        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > .5:
                class_id = detection[1]
                class_name = self.getName(class_id)
                print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
                box_x = detection[3] * self.image_width
                box_y = detection[4] * self.image_height
                box_width = detection[5] * self.image_width
                box_height = detection[6] * self.image_height
                if class_name == 'person':
                    target_pos.append([(detection[3] + detection[5]) / 2, detection[6]])
                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
                cv2.putText(image, class_name, (int(box_x), int(box_y+.05*self.image_height)), cv2.FONT_HERSHEY_SIMPLEX, (.005*self.image_width), (0, 0, 255))
        power = self.target.setTarget(target_pos)
        return int(power)

    ##
    # @brief リリース関数
    # @details カメラをリリースする
    # @return None
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

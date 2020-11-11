from detection import Detection


def main():
    i = 0
    detecter = Detection()
    while(i < 100):
        i += 1
        detecter.detect()
    detecter.release()


if __name__ == '__main__':
    main()
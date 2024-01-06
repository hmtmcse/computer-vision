import cv2


class BasicOCV:

    def show_image(self):
        image = cv2.imread("../resources/img/1875791.jpg")
        cv2.imshow("Show Image", image)
        cv2.waitKey(0)

    def play_video(self):
        video = cv2.VideoCapture("../resources/vdo/road-only-small.mp4")
        while video.isOpened():
            status, image = video.read()
            if not status:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            cv2.imshow("Play Video", image)

            if cv2.waitKey(1) == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

    def show_default_webcam(self):
        video = cv2.VideoCapture(0)
        while video.isOpened():
            status, image = video.read()
            if not status:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            cv2.imshow("Show Webcam", image)

            if cv2.waitKey(1) == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()


basic_ocv = BasicOCV()
basic_ocv.show_default_webcam()

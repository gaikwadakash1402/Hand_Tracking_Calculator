import cv2
from cvzone.HandTrackingModule import HandDetector
from gesture_recognition import GestureRecognizer
from calculator import Calculator


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1, detectionCon=0.8)
    recognizer = GestureRecognizer()
    calc = Calculator()

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            gesture = recognizer.recognize(fingers)
            if gesture:
                if gesture == 'C':
                    calc.reset()
                else:
                    calc.input(gesture)

        cv2.rectangle(img, (0, 0), (640, 50), (0, 0, 0), -1)
        cv2.putText(img, f"Expr: {calc.expression}", (10, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Hand Tracking Calculator", img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
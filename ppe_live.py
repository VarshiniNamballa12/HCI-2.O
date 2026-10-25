
from pathlib import Path

import cv2
from ultralytics import YOLO

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "best.pt"
CONFIDENCE = 0.35

def main():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    model = YOLO(str(MODEL_PATH))
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError(
            "Could not open webcam. Check camera permissions "
            "and close other apps using it."
        )

    print("PPE detection running. Press Q to quit.")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Could not read a frame from the webcam.")
                break

            results = model.predict(
                source=frame,
                conf=CONFIDENCE,
                verbose=False,
            )

            annotated_frame = results[0].plot()
            cv2.imshow("Viswakarma - PPE Safety Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

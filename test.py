from picamera2 import Picamera2, Preview
import time

class CameraApp():
    def __init__(self):
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)
    
    def start_preview(self):
        self.picam2.start_preview(Preview.QTGL)
        self.picam2.start()

    def run(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting Preview...")


if __name__ == "__main__":
    app = CameraApp()
    app.start_preview()
    app.run()

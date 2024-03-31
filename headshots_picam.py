import cv2
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

name = 'Manish' #replace with your name

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (512,304)})
picam2.configure(preview_config)
picam2.start()

img_counter = 0

while True:
    image = picam2.capture_array()
    cv2.imshow("Press space to take a photo", image)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape hit, closed")
        break
    elif k % 256 == 32:
        img_name = f"dataset/{name}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, image)
        print(f"{img_name} written!")
        img_counter += 1

cv2.destroyAllWindows()
picam2.stop()

import qrcode
img=qrcode.make("https://www.youtube.com/shorts/y_O3d3syd-A")
img.save("dhonims.jpg")

img=qrcode.make("i am ssm2 or s s mohith 79")
img.save("rolex.jpg")

import cv2
d=cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread("dhonims.jpg"))
print(val)

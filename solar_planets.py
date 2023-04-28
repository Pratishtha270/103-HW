import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (200,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (300,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Moon",
            (330,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (400,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (550,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (700,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (990,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("Output", img)

cv2.imwrite('Solar_system_with_name.jpg', img)

cv2.waitKey(0)
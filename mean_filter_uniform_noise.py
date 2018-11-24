import cv2
import numpy as np

inp_img = cv2.imread('D:/UDEMY/Computer Vision in Python/04 Image Segmentation/04-Codes/land.jpg')
gray_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Noisy Image", inp_img)

inp_img1 = gray_img.copy()

for x in range(1, inp_img.shape[0]-1):
    for y in range(1, inp_img.shape[1]-1):
        
        #we use 3x3 kernel window for the mean filter
        total = 0.0
        total = total + inp_img1[x,y]        #centre pixel
        total = total + inp_img1[x-1,y]      #left
        total = total + inp_img1[x-1,y+1]    #bottom left
        total = total + inp_img1[x,y+1]      #bottom
        total = total + inp_img1[x+1,y+1]    #bottom right
        total = total + inp_img1[x+1,y]      #right
        total = total + inp_img1[x+1,y-1]    #top right
        total = total + inp_img1[x,y-1]      #top
        total = total + inp_img1[x-1,y-1]    #top left
        
        inp_img1[x,y] = int(total/9)        #average of all the pixels in the 3x3 kernel window
        

cv2.imshow("Mean Fltered Image", inp_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
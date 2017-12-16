import cv2
import numpy as np 

img1=cv2.imread('baboon.jpg')
img2=cv2.imread('lena.jpg')
img3=cv2.imread('barbara.jpg')
img4=cv2.imread('Cameraman.bmp')

res1cub=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
res2cub=cv2.resize(img2,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
res3cub=cv2.resize(img3,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
res4cub=cv2.resize(img4,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

res1lin=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
res2lin=cv2.resize(img2,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
res3lin=cv2.resize(img3,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
res4lin=cv2.resize(img4,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)

res1nea=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
res2nea=cv2.resize(img2,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
res3nea=cv2.resize(img3,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
res4nea=cv2.resize(img4,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)

res1are=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
res2are=cv2.resize(img2,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
res3are=cv2.resize(img3,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
res4are=cv2.resize(img4,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)

#I like this interpolation the most
res1lan=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
res2lan=cv2.resize(img2,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
res3lan=cv2.resize(img3,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
res4lan=cv2.resize(img4,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)

cv2.imwrite('baboon_cubic.jpg',res1cub)
cv2.imwrite('lena_cubic.jpg',res2cub)
cv2.imwrite('barbara_cubic.jpg',res3cub)
cv2.imwrite('Cameraman_cubic.bmp',res4cub)

cv2.imwrite('baboon_linear.jpg',res1lin)
cv2.imwrite('lena_linear.jpg',res2lin)
cv2.imwrite('barbara_linear.jpg',res3lin)
cv2.imwrite('Cameraman_linear.bmp',res4lin)

cv2.imwrite('baboon_nearest.jpg',res1nea)
cv2.imwrite('lena_nearest.jpg',res2nea)
cv2.imwrite('barbara_nearest.jpg',res3nea)
cv2.imwrite('Cameraman_nearest.bmp',res4nea)

cv2.imwrite('baboon_area.jpg',res1are)
cv2.imwrite('lena_area.jpg',res2are)
cv2.imwrite('barbara_area.jpg',res3are)
cv2.imwrite('Cameraman_area.bmp',res4are)

cv2.imwrite('baboon_lanczos4.jpg',res1lan)
cv2.imwrite('lena_lanczos4.jpg',res2lan)
cv2.imwrite('barbara_lanczos4.jpg',res3lan)
cv2.imwrite('Cameraman_lanczos4.bmp',res4lan)
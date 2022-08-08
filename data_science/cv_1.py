import cv2
import numpy as np

im = cv2.imread(r'C:\Users\ZAID\Pictures\cosmere.jpg')

if im is None:
    print('Image not found')
else:
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_inv = cv2.bitwise_not(im_gray)
    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    im_lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
    im_luv = cv2.cvtColor(im, cv2.COLOR_BGR2LUV)
    im_xyz = cv2.cvtColor(im, cv2.COLOR_BGR2XYZ)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)

    cv2.imshow('cosmere', im)
    cv2.imshow('cosmere_bw', im_gray)
    cv2.imshow('cosmere_inv', im_inv)
    cv2.imshow('cosmere_rgb', im_rgb)
    cv2.imshow('cosmere_hsv', im_hsv)
    cv2.imshow('cosmere_lab', im_lab)
    cv2.imshow('cosmere_luv', im_luv)
    cv2.imshow('cosmere_xyz', im_xyz)
    cv2.imshow('cosmere_ycrcb', im_ycrcb)

    # save
    cv2.imwrite('data_science/cosmere_bw.jpg', im_gray)
    cv2.imwrite('data_science/cosmere_inv.jpg', im_inv)
    cv2.imwrite('data_science/cosmere_rgb.jpg', im_rgb)
    cv2.imwrite('data_science/cosmere_hsv.jpg', im_hsv)
    cv2.imwrite('data_science/cosmere_lab.jpg', im_lab)
    cv2.imwrite('data_science/cosmere_luv.jpg', im_luv)
    cv2.imwrite('data_science/cosmere_xyz.jpg', im_xyz)
    cv2.imwrite('data_science/cosmere_ycrcb.png', im_ycrcb)

    cv2.waitKey(0) # k is capital K
import xxlimited
import cv2

path = r'C:\Users\ZAID\Pictures\pikachu_hi_pokemon.jpg'
img = cv2.imread(path)

if img is None:
    print("i have done a blunder")

# resize image
h, w, _ = img.shape     # height, width, channels
img = cv2.resize(img,(w//2, h//2)) # half size

# change brightness
bright_img = cv2.add(img, 50)
dark_img = cv2.add(img, -50)

# flip image
flip_img = cv2.flip(img, 1) # 1 = horizontal flip
fliplr_img = cv2.flip(img, 0) # 0 = vertical flip

# stitch images
stitched_h_img = cv2.hconcat([img, flip_img, fliplr_img])
stitched_v_img = cv2.vconcat([img, flip_img, fliplr_img])

# show image
cv2.imshow('original', img)
cv2.imshow('bright', bright_img)
cv2.imshow('dark', dark_img)
cv2.imshow('flip', flip_img)
cv2.imshow('fliplr', fliplr_img)
cv2.imshow('stitched_h', stitched_h_img)
cv2.imshow('stitched_v', stitched_v_img)
cv2.waitKey(0)
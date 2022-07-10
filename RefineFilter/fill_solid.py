import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
 
def FillHole(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    len_contour = len(contours)
    contour_list = []
    for i in range(len_contour):
        drawing = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv2.drawContours(drawing, contours, i, (255, 255, 255), -1)
        contour_list.append(img_contour)
 
    out = sum(contour_list)
    return out

def FillHole255(input_bound):
    data_tmp = input_bound
    if data_tmp.max()>1:
        mask_out = FillHole(data_tmp)
    else:
        mask_out = data_tmp
    mask_out[mask_out > 0] = 255
    return mask_out

img_num = raw_data.shape[0]

for img_i in range(350,img_num):
    print(img_i)
    seg_raw = raw_data[img_i]
    seg_raw0 = seg_raw.astype('uint8')
    
    seg_raw0 = FillHole255(seg_raw0)
    plt.imshow(seg_raw0, cmap = 'gray')
    plt.show()
    
    print(seg_raw0.shape)
    print(np.max(seg_raw0))
    
    raw_data[img_i]=seg_raw0
    
    tif.imsave('mask_CM_solid.tif', raw_data)

from PIL import Image
from scipy import misc, ndimage
import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
import imageio


## 90~270 Image Augmentation
def Image_Aug(img_files, path1, path2):
    for ang in range(90,360,90):
        for i in img_files:
            if i.endswith('.jpg') or i.endswith('.JPG'):
                img1 = Image.open(path1 + i)
                im_rotate = img1.rotate(ang, expand = True)
                im_rotate.save(path2+str(ang)+"_"+i)

## 90~270 yolo_label Augmentation
def Label_Aug(lab_files, L_path1, L_path2):

    for ang in range(90,360,90):
        for j in lab_files:
            if j.endswith('.txt'):
                locat1 = L_path1 + j
                locat2 = L_path2 + str(ang)+ "_" + j
                txt = open(locat1, "r")
                lines = txt.readlines()  ## read each line
                ## use " " parse whole string to a list  
                for line in lines:
                    rl_line = line.split(" ")
                    rl_line[4] = rl_line[4][:8]  ## delete final element: "\n"

                    category, x_cent_bbox, y_cent_bbox, w_bbox, h_bbox = rl_line[0:5]
                    
                    ## new_x = old_y   new_y = 1(表示圖的全寬or高) - old_y  w,h互換
                    if ang == 90:
                        nx_cent_bbox = y_cent_bbox
                        ny_cent_bbox = format((1 - float(x_cent_bbox)), ".6f")  
                        nw_bbox = h_bbox
                        nh_bbox = w_bbox
                        new_label = [category, nx_cent_bbox, ny_cent_bbox, nw_bbox, nh_bbox]
                        # print(new_label)

                        new_txt = open(locat2, "a")
                        new_txt.write(" ".join( [str(l) for l in new_label] ) + "\n")

                    ## new_x = 1- old_y   new_y = 1 - old_y   w,h沒換
                    elif ang == 180:
                        nx_cent_bbox = format((1 - float(x_cent_bbox)), ".6f")
                        ny_cent_bbox = format((1 - float(y_cent_bbox)), ".6f")
                        nw_bbox = w_bbox
                        nh_bbox = h_bbox
                        new_label = [category, nx_cent_bbox, ny_cent_bbox, nw_bbox, nh_bbox]
                        #print(new_label)

                        new_txt = open(locat2, "a")
                        new_txt.write(" ".join( [str(l) for l in new_label] ) + "\n")

                    ## new_x = 1- old_y   new_y = old_y  w,h互換
                    elif ang == 270:
                        nx_cent_bbox = format((1 - float(y_cent_bbox)), ".6f")
                        ny_cent_bbox = x_cent_bbox
                        nw_bbox = h_bbox
                        nh_bbox = w_bbox
                        new_label = [category, nx_cent_bbox, ny_cent_bbox, nw_bbox, nh_bbox]
                        #print(new_label)
                        
                        ## 開新的txt檔並續寫新labels
                        new_txt = open(locat2, "a")
                        new_txt.write(" ".join( [str(l) for l in new_label] ) + "\n")
        print(new_txt)
        new_txt.close()
        txt.close()
        

def small_ang_Aug(files, path1, path2):
    ang = 10
    for i in files:
        if i.endswith('.jpg') or i.endswith('.JPG'):
            img1 = Image.open(path1 + i)
            im_rotate = img1.rotate(ang, expand = True)
            im_rotate.save(path2+str(ang)+"_"+i)


if __name__ == '__main__':

    path1 = "D:/My_Class/Paper/YUV/51/05/Imgs/Test/Ori/"
    path2 = "D:/My_Class/Paper/YUV/51/05/Imgs/Test/3dirs/"

    L_path1 = "D:/My_Class/Paper/YUV/51/05/Label/Test/Ori/"
    L_path2 = "D:/My_Class/Paper/YUV/51/05/Label/Test/3dirs/"
    
    img_files = os.listdir(path1)
    lab_files = os.listdir(L_path1)

    #print(img_files)

    
    Label_Aug(lab_files, L_path1, L_path2)
    # Image_Aug(img_files, path1, path2)

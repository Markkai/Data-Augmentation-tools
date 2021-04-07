import cv2
import os
import numpy as np
import math
from skimage import io, data, color
from matplotlib import pyplot as plt
from PIL import Image


def wholeImg_YUV(files, inputFolder, outputFolder):

    for img in files:
        if img.endswith('.jpg') or img.endswith('.JPG'):
            '''opencv open Image方法'''
            images = cv2.imread(inputFolder + img)
            YIQ_img = cv2.cvtColor(images, cv2.COLOR_BGR2YUV)

            '''PIL open Image方法'''
            # images = Image.open(inputFolder+img)
            # YIQ_img = color.rgb2yiq(images)
            Y,I,Q = cv2.split(YIQ_img) 
            hight, width, channel = YIQ_img.shape

            '''灰階照片pixel值:0~255; Y_min = 0; Y_max = 255'''
            for i in range(hight):
                for j in range(width):
                    '''((Y[i][j]-0) / (255-0))**0.8 可調照片亮度'''
                    Y[i][j] = (((Y[i][j]-0) / (255-0))**0.7)*255
        
            New_YIQ = cv2.merge([Y,I,Q])
            #New_RGB = color.yiq2rgb(New_YIQ)
            New_RGB = cv2.cvtColor(New_YIQ, cv2.COLOR_YUV2BGR)

            '''Show Images'''
            # cv2.imshow("showWindow", New_RGB)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            ''' 存圖片 '''
            img = "YIQ_" + img
            print(img)
            cv2.imwrite(outputFolder+img, New_RGB)
            

def cross_YUV(files, inputFolder, outputFolder, out_files):
    for img in files:
        if img.endswith(".jpg") or img.endswith(".JPG"):
            if "Lcl200_YUV09_"+ img in out_files:
                continue
            images = cv2.imread(inputFolder + img)
            YUV_img = cv2.cvtColor(images, cv2.COLOR_BGR2YUV)
            Y, U, V = cv2.split(YUV_img)
            hight, width, chanel = YUV_img.shape
            print(hight, width, chanel)

            color = ('y')
            for i , col in enumerate(color):
                hist = cv2.calcHist([YUV_img], [i], None, [256], [0, 256])
                plt.plot(hist, color=col)
                plt.xlim([0,256])
            # plt.show()
            # plt.savefig(outputFolder + "orighis_"+img)
            # plt.close()

            for i in range(hight):
                for j in range(width):
                    cross_ary = []
                    ## Cross Size
                    size = 100     
                    ## 透過減去與增加Cross的size若超出img的長寬範圍就無視此pixel否則加進Cross內
                    for p in range(1,size,1):
                        if i-p < 0:
                            continue
                        else:
                            cross_ary.append(Y[i-p][j])
                    for p in range(1,size,1):
                        if i+p >= hight:
                            continue
                        else:
                            cross_ary.append(Y[i+p][j])
                    for p in range(1,size,1):
                        if j-p < 0:
                            continue
                        else:
                            cross_ary.append(Y[i][j-p])
                    for p in range(1,size,1):
                        if j+p >= width:
                            continue
                        else:
                            cross_ary.append(Y[i][j+p])
                    # print(cross_ary)
                    Max_p = max(cross_ary)
                    Min_p = min(cross_ary)
                    son = abs(Y[i][j]-Min_p)
                    mom = Max_p-Min_p
                    ## gamma 值設定
                    gamma = 0.9
                    if son < 0:
                        int(math.ceil(son))
                    elif mom < 0:
                        int(math.ceil(mom))
                    elif mom == 0:
                        mom = 255
                    Y[i][j] = (((son) / (mom))**gamma)*255

            New_YUV = cv2.merge([Y,U,V])
            New_RGB2 = cv2.cvtColor(New_YUV,cv2.COLOR_YUV2BGR)
            n_color = ('y')
            for i , col in enumerate(n_color):
                hist = cv2.calcHist([New_YUV], [i], None, [256], [0, 256])
                plt.plot(hist, color=col)
                plt.xlim([0,256])
            # plt.show()
                # plt.savefig(outputFolder + "Processhis_"+img)
                # plt.close()

            img = "Lcl200_YUV09_"+ img
            print(img)
            cv2.imwrite(outputFolder+img, New_RGB2)
            print("Saved")
            

if __name__ == '__main__':

    inputFolder = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/Original_Datas/current_total/Original/"
    outputFolder = "D:/My_Class/Paper/YUV/201/09/"
    files = os.listdir(inputFolder)
    out_files = os.listdir(outputFolder)
    # print(files)
    cross_YUV(files, inputFolder, outputFolder, out_files)

#    wholeImg_YUV(files, inputFolder, outputFolder)
import cv2
import os
import numpy as np

def hisEqColor(files, inputFolder, outputFolder):

    for img in files:
        if img.endswith(".jpg") or img.endswith(".JPG"):
            images = cv2.imread(inputFolder + img)
            ycrcb = cv2.cvtColor(images, cv2.COLOR_BGR2YCR_CB)
            channels = cv2.split(ycrcb)
            cv2.equalizeHist(channels[0], channels[0]) ## equalizeHist(in, out)
            cv2.merge(channels, ycrcb)
            img_eq = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR)

            img = "YCR_" + img
            cv2.imwrite(outputFolder + img, img_eq)


def gray_world(files, inputFolder, outputFolder):

    for img in files:
        if img.endswith(".jpg") or img.endswith(".JPG"):
            images = cv2.imread(inputFolder + img)

            images = images.transpose(2, 0, 1).astype(np.uint32)
            avgB = np.average(images[0])
            avgG = np.average(images[1])
            avgR = np.average(images[2])

            avg = (avgB + avgG + avgR) / 3

            images[0] = np.minimum(images[0] * (avg / avgB), 255)
            images[1] = np.minimum(images[1] * (avg / avgG), 255)
            images[2] = np.minimum(images[2] * (avg / avgR), 255)

            new_img = images.transpose(1,2,0).astype(np.uint8)
            img = "GW_" + img 
            cv2.imwrite(outputFolder + img, new_img)
            
if __name__ == "__main__":
    
    inputFolder = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1030_train/Train_pics/Zero/"
    outputFolder = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1030_train/Train_pics/Gray_world/"
    files = os.listdir(inputFolder)

    # hisEqColor(files, inputFolder, outputFolder)
    gray_world(files, inputFolder, outputFolder)
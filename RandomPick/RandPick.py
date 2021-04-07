import os, random, shutil, time
from classes import brand
import numpy as np

random.seed(time.time())

def moveFile(ImageDir):
    pathdir = os.listdir(ImageDir)
    total_num = len(pathdir)
    pick_num = int(total_num*0.15)
    sample = random.sample(pathdir, pick_num)
    print(sample)
    for name in sample:
        shutil.move(ImageDir + name, tarDir + name)
        

def pickYuvPics(fileDir, ImageDir, tarDir, testDir):
    imgdir = os.listdir(ImageDir)
    refdir = os.listdir(fileDir)

    # print(refdir)
    Rdicts = {}
    dicts = {}
    for rname in refdir:
        v = 0
        v += 1
        Rdicts[rname] = v
    # print(imgdir)
    # print(Rdicts.keys())

    for name in imgdir:
        s_name = name[12:]
        print(s_name)
        for i in Rdicts.keys():
            if s_name == str(i):
                shutil.move(ImageDir+name, testDir + name)
                print("test: ", name)

   
if __name__ == '__main__':

    # YUV_allImg 位置
    ImageDir = "D:/My_Class/Paper/YUV/51/05/Total_pics/"
    # train_位置
    fileDir = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1231_Ori+YUV+Rot/Test_pics/Ori_test/"
    # YUV_train 位置
    tarDir = "D:/My_Class/Paper/YUV/51/05/Imgs/Train/"
    # testImg 位置
    testdir = "D:/My_Class/Paper/YUV/51/05/Imgs/Test/"
    

    # moveFile(ImageDir)
    pickYuvPics(fileDir, ImageDir, tarDir, testdir)
    # pickYUV_Test(testdir, ImageDir)


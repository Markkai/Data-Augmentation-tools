import os
import numpy as np
import pandas as pd
from classes import brand


## 紀錄各類別出現在哪幾張圖片內
def classes_files(classes, Label):
    files = os.listdir(Label)
    c_dict = {}

    for file in files:
        if file.endswith("txt"):
            r_file = Label + file
            txt =  open(r_file, 'r')
            lines = txt.readlines()
            for line in lines:
                line = line.split(" ")
                idx = int(line[0])
                if idx not in c_dict.keys():
                    dic = {idx : [file]}
                    c_dict.update(dic)
                else:
                    c_dict[idx].append(file)
    keys = c_dict.keys()
    sort_keys = []
    for ky in keys:
        sort_keys.append(ky)
        sort_keys.sort()
    sort_c_dict = {}
    for i in sort_keys:
        val = [len(set(c_dict.get(i))), set(c_dict.get(i))]  ## set()可移除重複的value值
        tmp = {i : val}   
        sort_c_dict.update(tmp)
    # print(sort_c_dict)

    outputfilename = "cls_files_Currentall.txt"
    outfile = Label + outputfilename
    for ky in sort_c_dict.keys():
        idx = ky
        clsname = classes[ky]
        files = str(sort_c_dict.get(ky))
        Ftxt = open(outfile, 'a')
        Line = [str(idx), " ", clsname, ",", files, "\n" ]
        Ftxt.writelines(Line)
    Ftxt.close()

## 記錄各類別出現總次數 Test or Train set Ground truth counts
def Class_Lable_count(classes, testLabel):
    files = os.listdir(testLabel)
    b_dict = {}
    
    for file in files:
        if file.endswith("txt"):
            r_file = testLabel + file    ## testlabel路徑 + 檔名
            txt = open(r_file, 'r')
            lines = txt.readlines()      ## 逐行讀取
            for line in lines:
                line = line.split(" ")
                idx = int(line[0])
                if idx not in b_dict.keys():
                    dic = {idx : [idx]}
                    b_dict.update(dic)
                else:
                    b_dict[idx].append(idx)

    keys = b_dict.keys()
    sort_key = []
    for key in keys:
        sort_key.append(key)
        sort_key.sort()
    ## Print keys length
    # print(len(sort_key))
    Label_dict = {}
    Label_dict2 = {}
    # 找出資料集共包含幾種類，以及各類的數量並印出來
    for brand in sort_key:
        #print(brand + " : " + str(len(b_dict.get(brand))))
        dicts = {brand : str(len(b_dict.get(brand)))}
        dicts2 = {brand : str(b_dict.get(brand))}
        Label_dict.update(dicts)
        Label_dict2.update(dicts2)

    # print(testLabel)
    outputfilename = "all_YUV_Test_GT.txt"
    outfile = testLabel + outputfilename
    for key in Label_dict.keys():
        # print(classes[key] + ": " + testLabel.get(key))
        idx = key
        cls_name = classes[key]
        numbers = Label_dict.get(key)
        files = Label_dict2.get(key)
        Gtxt = open(outfile, 'a')
        L = [str(idx), " " , cls_name , ",", numbers,"\n"]
        Gtxt.writelines(L) 
        Gtxt.close()

def Label_counts(Labelfile):
    counts = 0
    files = os.listdir(Labelfile)
    
    for file in files:
        if file.endswith(".txt"):
            r_file = Labelfile + file
            txt = open(r_file, 'r')
            lines = len(txt.readlines())
            counts += lines
    print(counts)

if __name__ == "__main__":

    imgpath = "D:/YOLO_Base/darknet-master_V4/darknet-master/build/darknet/x64/testresult/1030/"
    rstpath = "D:/YOLO_Base/darknet-master_V4/darknet-master/build/darknet/x64/results/1116/"
    Labels = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/all_YUV_Test/tests/"
    classes = brand()

    # images = os.listdir(imgpath)
    # results = os.listdir(rstpath)
    

    # classes_files(classes, Labels)
    Class_Lable_count(classes, Labels)
    # Label_counts(Labels)
    
    

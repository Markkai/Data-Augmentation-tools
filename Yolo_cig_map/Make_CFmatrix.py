import os
import openpyxl
import pandas as pd
import xlrd
import xlwt
from xlutils.copy import copy
import codecs
from openpyxl.utils import get_column_letter
from collections import Counter
import time

excel = "200x200_07YUV_Rot.xls"
Aps = "200x200_07YUV_Rot_Aps.txt"
Fps = "200x200_07YUV_Rot_TpFps.txt"
testGt = "all_YUV_Test_GT.txt"


## 將TPs FPs 貼到xls內
def txt_2xls(filepath, output):
    
    xlsfile = output + excel
    workbook = xlrd.open_workbook(xlsfile)
    sheet1 = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheet1[0])
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    # 將 Aps.txt內容存到xls的row列內，存各類名(row[0])與label數量(row[1])(Ground Truth)
    f4 = open(filepath + Aps)
    
    c1 = 1 ## 從col[1]開始
    while True:
        r = 0
        line = f4.readline()
        if not line:
            break
        # print(line)
        for i in range(len(line.split(","))):
            if i == 1:  break 
            if line.split(",")[1] == "0" and line.split(",")[2] == "0": 
                c1 = c1 - 1
                break
            else:
            ## 跳過FP numbers
                item = line.split(",")[i]       ## Ex 0 Name,1,1 從,切開, item= class name
                item2 = line.split(",")[i+1]    ## item2 = Tp
                new_worksheet.write(r,c1,item)         ## r=row, c1=col, item=line[i]
                r += 1                          ## Next row 儲存
                new_worksheet.write(r,c1,item2)
        c1 += 1
    new_workbook.save(xlsfile)

    # Aps.txt內各類名存到col[0]整行內(Predicted)
    f5 = open(filepath + Aps)
    r2 = 3 ## 從row[2]開始
    while True:
        line2 = f5.readline()
        if not line2:
            break
        for i in range(1):
            item2 = line2.split(",")[i]
            new_worksheet.write(r2,i,item2)
        r2 += 1
    new_workbook.save(xlsfile)
    f5.close()
    f4.close()

## 將testGt 真正Ground Truth Label數量貼到xls row[1]中
def txtGt_2xls(filepath, output):

    xlsfile2 = output + excel
    test_Gt = filepath + testGt
    workbook2 = xlrd.open_workbook(xlsfile2)
    new_workbook2 = copy(workbook2)
    new_worksheet2 = new_workbook2.get_sheet(0)
    faps = open(filepath + Aps)
    f4_1 = open(test_Gt)
    lines1 = faps.readlines()
    c2 = 1
    lin2_ct = 0
    line2 = f4_1.readlines()
    for line in lines1 :
        line2[lin2_ct]
        r2 = 0
        if not line:
            break
        for i in range(len(line.split(","))):
            if i == 1:  break
            if line.split(",")[i] == line2[lin2_ct].split(",")[i].strip("\n"):
                r2 += 1
                value = line2[lin2_ct].split(",")[1]
                # print(value)
                new_worksheet2.write(r2,c2,value)
            elif line.split(",")[i] != line2[lin2_ct].split(",")[i].strip("\n"):
                lin2_ct = lin2_ct - 1
        c2 += 1
        lin2_ct += 1

    new_workbook2.save(xlsfile2)
    f4_1.close()
    faps.close()


## 將APs.txt內的 TPs 映射到對應的class 1116_CFmatx.xls檔內
def Tps_2xls(filepath, output):
    xlsfile = output + excel
    f = open(filepath + Aps)
    f_a = open(filepath + "200x200_07YUV_Rot.txt", "a")  
    workbook = xlrd.open_workbook(xlsfile)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    f_line = f.readline()
    for c in range(1,worksheet.ncols):
        f_line = f_line.split(",")
        r = c+2     ## col[1]時 Tp要印在row[3]        
        TP_value = f_line[1]    ## [0 Dunhill_gold_s, 20,0]
        Gt_value = worksheet.cell_value(1, c)
        FN = int(Gt_value) - int(TP_value)  ## False Negative =  Groud Truths - True Positive
        new_worksheet.write(r, c, TP_value)
        new_worksheet.write(2, 0, "FNs")
        new_worksheet.write(2, c, str(FN))

        new_L = [f_line[0] + "," + f_line[1] + "," + f_line[2].strip("\n") + "," + str(FN) + "\n"]
        f_a.writelines(new_L)
        f_line = f.readline()
    new_workbook.save(xlsfile)



## 將 TpFps.txt內的 FPs 映射到對應的class 1116_CFmatx.xls檔內
def Fps_2xls(filepath, output):

    Fpsfile = filepath + Fps
    # Mapsfile = filepath + "1116_Map.txt"
    xlsfile = output + excel
    f_txt = open(Fpsfile)
    workbook = xlrd.open_workbook(xlsfile)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])

    ## GT: 153
    ## Det: 143
    Gt_idx = []
    Pd_idx = []
    lines = f_txt.readlines()
    
    ## 分解Fps.txt每行內容  擷取txt內 Det: idx
    for idx in range(1,len(lines),2):
        Fp_Pdidx = (lines[idx].split(":")[1]).strip("\n")  
        Fp_Pdidx = Fp_Pdidx.strip(" ")

        ## 擷取 Excel xls檔 的 rows (Predicted)
        for i in range(worksheet.nrows):
            ## sheet.cell_value(row,col)
            Pdidx = (worksheet.cell_value(i,0).split(" ")[0].strip(" ")) ## 將name切成: [0,Dunhill_gold_s] 擷取[0] 
            if Pdidx == Fp_Pdidx:
                Pd_idx.append(i) ## 預測的類別對應到xls的row index
                break
    
    ## 分解Fps.txt每行內容
    for idx in range(0,len(lines),2):
        Fp_Gtidx = (lines[idx].split(":")[1]).strip("\n")  
        Fp_Gtidx = Fp_Gtidx.strip(" ")
        # print(Fp_Gtidx)

        ## 擷取 Excel xls檔 的 columns (Predicted)
        for j in range(worksheet.ncols):       
            # print("idx:",j, worksheet.cell_value(0, j))
            Gtidx = (worksheet.cell_value(0, j).split(" ")[0]).strip(" ")
            if Gtidx == Fp_Gtidx:
                Gt_idx.append(j)  ## Gt類別對應到xls的column index
                break
    Gt_dict = {}
    Pd_dict = {}
    ## 重複的類別記錄成 index : counts 型式
    for i in Gt_idx:
        if Gt_idx.count(i) >= 1:
            Gt_dict[i] = Gt_idx.count(i)
    ## 將count結果存成 newGt_idx list
    newGt_idx = list(Gt_dict.keys()) 
    
    for i in Pd_idx:
        if Pd_idx.count(i) >= 1:
            Pd_dict[i] = Pd_idx.count(i)    
    ## 將count結果存成 newPd_idx list
    newPd_idx = list(Pd_dict.keys())
    # print(Gt_idx)
    # print(Pd_idx)
    # print(Gt_dict)
    # print(Pd_dict)
    # print(newGt_idx)
    # print(newPd_idx)

    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    PGs_dict = {}
    for i in range(len(Pd_idx)):
        if Pd_idx[i] not in PGs_dict:
            PGs_dict[Pd_idx[i]] = [Gt_idx[i]]
        else:
            PGs_dict[Pd_idx[i]].append(Gt_idx[i])
    print(PGs_dict)

    count_vList = []
    for k,v_list in PGs_dict.items():
        # print(k)
        # print(v_list)
        tmp_list = []
        for i in v_list:
            if v_list.count(i) >= 1:
                cts = [i ,v_list.count(i)]
                tmp_list.append(cts)
        count_vList.append(tmp_list)
    # print(count_vList)    
    # print(count_vList[1][0][0])

    ## 存放row座標
    ridxs = []
    for i in PGs_dict.keys():
         ridxs.append(i)
         
    for j in range(len(count_vList)):
        # print(count_vList[j])
        for ele in range(len(count_vList[j])):
            ridx = ridxs[j]
            cidx = count_vList[j][ele][0]
            value = count_vList[j][ele][1]
            new_worksheet.write(int(ridx), int(cidx), value)
            # print(ridx,cidx,value)

    new_workbook.save(xlsfile)


if __name__ == "__main__":

    txtFiles_path = "C:/Users/user/Desktop/Class/Cigarette_Brand/Tools/Yolo_cig_map/Maps/CF_matrix/200x200_07YUV+Rot/needs_files/"
    excelFile = "C:/Users/user/Desktop/Class/Cigarette_Brand/Tools/Yolo_cig_map/Maps/CF_matrix/200x200_07YUV+Rot/"
    


    txt_2xls(txtFiles_path, excelFile)
    txtGt_2xls(txtFiles_path, excelFile)
    Tps_2xls(txtFiles_path, excelFile)
    Fps_2xls(txtFiles_path, excelFile)
    





import pandas as pd
import numpy as np

v3 = "D:/YOLO_Base/modifie_darknetv3/darknet-master/build/darknet/x64/results/2021_0217_Ori+200x200_07YUV+Rot/Recalculate_Maps.txt"
v4 = "D:/YOLO_Base/darknet-master_V4/darknet-master/build/darknet/x64/results/20210222_200x200_07YUV+Rot/Recalculate_Maps.txt"
count = 0
sums = 0
rl_map = 0
worst = []
Map_f = open(v4)
lines = Map_f.readlines()

    
for line in lines:
    if line != '\n':
        
        ap = []
        num = ""
        line = line.split(" = ")   ## 用 = 號把內容切開
        # print(line[3])             ## Ex: ['class_id', '68, name', 'David_gold_s, ap', '42.86%          (TP', '3, FP', '0)\n']
        ap.append(line[3])         ## ap數值在index[3]內
        for i in ap:
            for j in i:
                if j == "%":       ## 逐行搜索遇到 % 停止
                    break
                else:    
                    num += j       ## 將char接在一起放入num
            new_num = float(num)   ## 將num轉float存進new_num  
            print(new_num)      
            if new_num >= 50.0:    ## threshhold >= 設定值者加入計算map
                count += 1
                sums += new_num
                rl_map = sums/count
            if new_num >= 1.0 and new_num <= 80.0:
                worst.append(line)
        print(count)
        print("Recalculate Maps: " , rl_map)
        print("==============================================================================================")
        for bd in worst:
            print(bd)
    else:
        break
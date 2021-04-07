import os
import pandas as pd
import numpy as np

conf_path = "D:/YOLO_Base/darknet-master_V4/darknet-master/build/darknet/x64/results/confidence/1116_1201/"
wash_path = os.path.join(conf_path, "wash")


files = os.listdir(conf_path)
for i in files:
    # print(i)
    old = i.split("test_")
    newname = old[1]
    # print(newname)
    with open( conf_path + i , 'r') as f1:
        lines = f1.readlines() 
    f2 = open(wash_path + newname, 'w')
    for line in lines:
        cont = line.split(" ")
        cof = cont[1]
        if float(cof) < 0.5:
            continue
        else:
            f2.write(line)
        
        
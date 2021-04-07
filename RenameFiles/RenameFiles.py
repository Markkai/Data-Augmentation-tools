import os, shutil
from collections import Counter


def re_name(source, destination):
    files = os.listdir(source)
    name = []
    for i in files:
        if i.endswith(".txt"):
            newname = "Lcl50_YUV05_"+ i
            # 參數1:舊名 , 參數2:新名
            shutil.copyfile(source + i, destination + newname)



""" shutil.copyfile 複製路徑內的檔案到其他路徑並重新命名 """
def cpyAndrename(source, destination, refpath):
    files = os.listdir(source)
    ref_file = os.listdir(refpath)
    name = []
    for j in ref_file:
        j = j.split(".")
        name.append(j[0])

    indx = 0
    for i in files:
        newname = name[indx] + ".txt"
        indx += 1
        #print(newname)
       # 參數1:舊名 , 參數2:新名
        shutil.copyfile(source+i, destination+newname)




if __name__ == '__main__':

    sorc = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1231_Ori+YUV+Rot/Test_label/Ori/"
    dest = "D:/My_Class/Paper/YUV/51/05/Label/Test/Ori/"

    refpath = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1030_train/Train_pics/Cross_YUV/11x11/4_dirct/"
    # ref_file = os.listdir(refpath)
    # print(ref_file)

    # re_name(sorc, dest)

    # cpyAndrename(sorc, dest, refpath)
    c = Counter("bella")
    print(c)
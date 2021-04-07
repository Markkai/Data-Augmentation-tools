import os, shutil

""" 將test或train圖片檔名存起來，用於挑出txt與xml Label檔 """
def namelist(files):
    name = ""
    namelist = []
    # 路徑內每個file
    for fname in files:     
        # 針對單一file檔名iterate，遇到 '.jpg' 暫存檔名進name變數
        if fname.endswith('.jpg') or fname.endswith('.JPG'):  
            fname = fname.strip(".jpg")
            fname = fname.strip(".JPG")
            namelist.append(fname)   # 將name存進namelist內        
    print(namelist)        
    print(len(namelist))
    return namelist

""" 挑出test或train的txt檔 """
def txtmove(txt_labelDir, namelist):
    txtname = []
    for i in namelist:
        i = i + ".txt"
        txtname.append(i)
    # print(txtname)
    for i in txtname:
        shutil.copyfile(txt_labelDir + i , target_labelDir + i)

""" 挑出test的xml檔 """
def xmlmove(xml_labelDir, namelist):
    xmlname = []
    for j in namelist:
        j = j + ".xml"
        xmlname.append(j)
    print(xmlname)
    for j in xmlname:
        shutil.copyfile(xml_labelDir + j , target_labelDir + j)

if __name__ == "__main__":
    fileDir = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1231_Ori+YUV+Rot/Train_pics/YUV/"
    txt_labelDir = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/Original_Datas/current_total/Cross_YUV/201x201/Label/"
   
    ## xml_labelDir = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1012_train/Train_label/xml/"
    target_labelDir = "C:/Users/user/Desktop/Class/Cigarette_Brand/Picture/Cargo_Pic/20200827_summarize/Original03+05/Pic/1231_Ori+YUV+Rot/Train_label/YUV/"

    files = os.listdir(fileDir)
    namelist(files)

    txtmove(txt_labelDir, namelist(files))
    # xmlmove(xml_labelDir, namelist(files))



## Precision = TP / TP+FP
def Calcu_Precision(txtPath):
    txtFile = txtPath + TpFn
    f = open(txtFile)
     
    lines = f.readlines()
    count = 0
    Total_Pre = 0
    Avg_Pre = 0
    for line in lines:
        line = line.split(",")
        if line[1] == "0" and line[2] == "0":
            continue
        else:
            count += 1
            each_Pre = int(line[1]) / (int(line[1]) + int(line[2]))
            Total_Pre += each_Pre
    Avg_Pre += Total_Pre / count
    print("All Rank avg Precision: ", Avg_Pre*100)
    return (Avg_Pre*100)

## Recall = TP / TP+FN
def Calcu_Recall(txtPath):
    txtFile = txtPath + TpFn
    f = open(txtFile)
    lines2 = f.readlines()
    count2 = 0
    Total_Rec = 0
    Avg_Rec = 0
    for line2 in lines2:
        line2 = line2.split(",")
        line2[3] = line2[3].strip("\n")

        if line2[1] == "0" and line2[3] == "0":
            continue
        else:
            count2 += 1
            each_Rec = int(line2[1]) / (int(line2[1]) + int(line2[3]))
            Total_Rec += each_Rec
    Avg_Rec += Total_Rec / count2
    print("All Rank avg Recall: ", Avg_Rec*100)
    return (Avg_Rec*100)

## F1 = (1+B^2) * (Pre*Recall) / ((B^2*Pre) + Recall)
def F1_Score(txtPath):
    Precision = Calcu_Precision(txtPath)
    Recall = Calcu_Recall(txtPath)
    Belta = 1
    F1 = (1 + Belta**2)*(Precision*Recall) / (((Belta**2) * Precision) + Recall)

    f_a = open(target_path + "0122_metrics.txt", "w") 
    new_L = ["All Rank avg Precision: ", str(Precision) , "\n" , "\nAll Rank avg Recall: ", str(Recall) , "\n" , "\nF1_Score: ", str(F1)]
    # print("All Rank avg Precision: ", Precision)
    f_a.writelines(new_L)



if __name__ == "__main__":

    txtFiles_path = "C:/Users/user/Desktop/Class/Cigarette_Brand/Tools/Yolo_cig_map/Maps/CF_matrix/20210122/needs_files/"
    target_path = "C:/Users/user/Desktop/Class/Cigarette_Brand/Tools/Yolo_cig_map/Maps/CF_matrix/20210122/"
    TpFn = "0114TpFpFn.txt"

    Calcu_Precision(txtFiles_path)
    Calcu_Recall(txtFiles_path)
    F1_Score(txtFiles_path)
import glob
import re
import numpy as num
import matplotlib as plt

folderdataset = list()
filedataset = list()

#### read data ##### 
folders = glob.glob("./data/*")
for foldername in folders:
    filedataset.clear()
#    print(foldername)#フォルダ名表示
    categories = glob.glob(foldername+"/*")
    for catename in categories:
#        print(catename)#カテゴリ名表示
        files = glob.glob(catename+"/*")
        for filename in files:
            if('result' in filename):
#                print(filename)#ファイル名表示
                f = open(filename, 'r', encoding='UTF-8')
                while True:
                  line = f.readline()
                  if line:
                    if('score' in line):
                        score = re.findall(':(.*)',line)
                    if('value' in line):
                        value = re.findall(':(.*)',line)
                    if('errro' in line):
                        errro = re.findall(':(.*)',line)
                  else:
                    break
                linedata = [float(score[0]),float(value[0]),float(errro[0])]
#                print(linedata)#ファイルから抽出したデータ
                filedataset.append(linedata)
    folderdataset.append(filedataset)
print(folderdataset)

print([row[0] for row in folderdataset])#cate列で抽出
print([row[0][1] for row in folderdataset])#cate列とtxtのsocoreの両条件で抽出

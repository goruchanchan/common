import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import csv

colorlist = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf','g','b']
titlelist = ['score', 'value', 'error']
scorePlt = []
valuePlt = []
errorPlt = []
Plots = []
labels = []

folderdataset = list()
filedataset = list()
scores = []#配列定義
values = []
errors = []


resultdirname = "summary/"
os.makedirs(resultdirname, exist_ok=True)

#### read data ##### 
folders = glob.glob("./data/*")#順番バラバラ
folders = sorted(folders)#順番ソート(数値が2桁になるとソートできないので注意)
#データ読み込み
for foldername in folders:
#    filedataset.clear()
#    print(foldername)#フォルダ名表示
    categories = sorted(glob.glob(foldername+"/*"))
    for catename in categories:
#        print(catename)#カテゴリ名表示
        files = sorted(glob.glob(catename+"/*"))
        for filename in files:
            if('result' in filename):
#                print(filename)#ファイル名表示
                f = open(filename, 'r', encoding='UTF-8')
                while True:
                  line = f.readline()
                  if line:
                    if('score' in line):
                        score = re.findall(':(.*)',line)
                        scores.append(float(score[0]))
                    if('value' in line):
                        value = re.findall(':(.*)',line)
                        values.append(float(value[0]))
                    if('errro' in line):
                        error = re.findall(':(.*)',line)
                        errors.append(float(error[0]))
                  else:
                    break

#scoresの前処理
#print(scores)
scores = np.reshape(scores,(len(folders),len(categories)))#行列変換(型:list->ndarray)
values = np.reshape(values,(len(folders),len(categories)))#行列変換(型:list->ndarray)
errors = np.reshape(errors,(len(folders),len(categories)))#行列変換(型:list->ndarray)
#print(scores)


#型変換(ndarray->list)
scoresOut = scores.tolist()
valuesOut = values.tolist()
errorsOut = errors.tolist()
#print(scores)
#print(values)
#print(errors)

#平均、標準偏差格納
tmpList=[]
for i in range(len(folders)):
    scoresOut[i] += [np.mean(scores[i]),np.std(scores[i])]
    valuesOut[i] += [np.mean(values[i]),np.std(values[i])]
    errorsOut[i] += [np.mean(errors[i]),np.std(errors[i])]
#print(scoresOut)
#print(valuesOut)
#print(errorsOut)

#ラベル生成
for category in categories:
    labels.append(category.split('/')[-1])#プロット用ラベル用意
labels+=['ave','std']#ラベル追加
#print(labels)

#一括表示用にリストへ格納

Plots.append(scoresOut)
Plots.append(valuesOut)
Plots.append(errorsOut)

print(Plots)
print(len(Plots))
i = 0
for plot in Plots: 
    fig,ax = plt.subplots(1,1,figsize=(20,8))
    ax.set_title(titlelist[i])#タイトル
    width = 0.2
    left = np.arange(len(scoresOut[0]))  # numpyで横軸を設定
    print(len(folders))
    print(plot)
    for j in range(len(folders)):
        height = plot[j] #代入
        plt.bar(left+width*j, height, color=colorlist[j], width=width,label=folders[j].split('/')[-1], align='center')#棒グラフを並べて表示するようにシフトさせていく
        for xval, yval in zip(range(len(labels)), height):#各棒グラフに値を挿入
            ax.text(xval+width*j, yval, '{:.2f}'.format(yval), ha='center', va='bottom')
    plt.xticks(left + width*(len(folders)/2), labels)
    plt.grid()#グリッドOn
    plt.legend()#凡例
    fig.savefig(resultdirname+titlelist[i]+".png")
    plt.show()
    i = i + 1

#ファイル出力
f = open(resultdirname+'summary.csv', 'w')
writer = csv.writer(f)
writer.writerow(folders)
writer.writerow(titlelist[0])
writer.writerow(scores.tolist())
writer.writerow(titlelist[1])
writer.writerow(values.tolist())
writer.writerow(titlelist[2])
writer.writerow(errors.tolist())
f.close()


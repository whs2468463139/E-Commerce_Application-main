import csv

def takeSecond(elem):
    return elem[1]

def compkey(keyword):
    print("compkey算法开始，种子关键词为“" + keyword + "”...")
    # midding是存储中介关键词候选词的文件，还未最终选取
    with open('midding.csv', 'w', encoding='utf-8') as file:
        print("清空候选关键词文件内容")
    with open('processed_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = list(reader)
        for i in range(len(result)):
            if result[i][0]==keyword:
                id=result[i][5]
                for j in range(max(0,i-9),min(i+9,len(result))):
                    if result[j][5]==id and result[j][0]!=keyword:
                        with open('midding.csv', 'a', encoding='utf-8') as f:
                            f.write("{0},{1}\n".format(result[j][0],result[j][1]))

    with open('midding.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = list(reader)
        result.sort(key=takeSecond,reverse = True)
        midKeyAndCompKey = []
        for i in range(len(result)):
            exist = 0
            for j in range(len(midKeyAndCompKey)):
                if midKeyAndCompKey[j][0]==result[i][0]:
                    exist=1
                    midKeyAndCompKey[j][1]=int(result[i][1])+int(midKeyAndCompKey[j][1])
                    break
            if exist!=1 and len(midKeyAndCompKey)<10:
                midKeyAndCompKey.append(result[i])
        midKeyAndCompKey.sort(key=takeSecond,reverse = True)

        with open('processed_data.csv', 'r', encoding='utf-8') as f:
            r = csv.reader(f)
            rst = list(r)
            ans = []
            for i in range(5):
                a=0
                ka=0
                sa=0
                for line in rst:
                   if line[0]==midKeyAndCompKey[i][0]:
                       a+=int(line[1])
                ka=int(midKeyAndCompKey[i][1])
                sa=int(midKeyAndCompKey[i+5][1])
                ans.append([i,float(ka)/float(a - sa)])
                print("中介关键词为："+midKeyAndCompKey[i][0]+"("+str(midKeyAndCompKey[i][1])+") "+"竞争关键词为："+midKeyAndCompKey[i+5][0]+"("+str(midKeyAndCompKey[i+5][1])+") "+"竞争度为："+str(ans[i][1]))

            print("竞争关键词通过关键字排序如下：")
            ans.sort(key=takeSecond,reverse = True)
            for i in range(5):
                print(midKeyAndCompKey[i+3][0], end=" ")
            print("\n")




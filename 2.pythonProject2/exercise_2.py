#①读取一个文本，并将其中单词按出现次数由大到小排列（不要考虑标点符号）
import re
with open("file.txt","r",encoding="UTF-8") as f:
    content=f.read()
    content=re.sub(r"[^\w\s]","",content)
    content=content.split(" ")
    print(content)
    words={ }
    for word in content:
        word=word.lower()
        if word not in words:
           words[word]=1
        else:
           words[word]+=1
    print(words)
    words=sorted(words.items(),key=lambda x:x[1],reverse=True)
    print(words)

#补充
# re.sub()函数，正则表达式(一种处理字符串的强大工具)，详细内容可以网上搜寻


#②读取一个文件。统计每门课的最高分以及对应同学姓名（返回列表）
dictionary={}
first={}
with open("file2.txt","r",encoding="UTF-8") as f:
    for line in f:
        line=line[:-1]      #去除每行的回车符
        curriculum,name,score=line.split("，")   #注意：去除的是中文逗号
        score=int(score)
        if curriculum not in dictionary:
            dictionary[curriculum]=[]
        if [name,score] not in dictionary[curriculum]:
            dictionary[curriculum].append([name,score])
    print(dictionary)
    i=0
    for key,value in dictionary.items():
        maxscore = 0
        maxname = ""
        for stu in value:
            if i==0:
                maxscore=stu[1]
                maxname=stu[0]
            else:
                if maxscore<stu[1]:
                    maxscore=stu[1]
                    maxname=stu[0]
            i+=1
        first[key]=[maxname,maxscore]
    print(first)


#补充：
# 按行读取文件返回的是字符串，因此需要使用split()函数返回一个列表
# 可以用多个变量依次接受列表的对应元素
#例子：
"""
stu=[1,2,3,4]
num1,num2,num3,num4=stu
print(num1,num2,num3,num4)
"""
# 除了列表以外，字符串也可以进行切片
#例子：
"""
word="HELLO"
word=word[:-1]
print(word)     #在终端显示HELL
"""

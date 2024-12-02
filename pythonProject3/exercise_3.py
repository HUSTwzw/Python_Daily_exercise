#①将学科老师的名字插入原有学生成绩文本
teacher=[]
student=[]
with open("file2.txt","r",encoding="utf-8") as f2:
    for line2 in f2:
        content2=line2[:-1]
        content2=content2.split("，")
        teacher.append(content2)

with open("file1.txt","r+",encoding="utf-8") as f1:
    inform=f1.readline()
    while(len(inform)>=1):
        content1=inform[:-1]
        content1=content1.split("，")
        student.append(content1)
        inform=f1.readline()

    place=0
    for stu in student:
        for tea in teacher:
            if tea[0] ==stu[0]:
                student[place].insert(0,tea[1])
                place+=1
    print(student)

    for stu in student:
        stuc=""
        for stucontent in stu:
            stuc+=f"{stucontent} "
        stuc+="\n"
        f1.write(stuc)


#②统计各个体育运动的参与人数
sports={}
with open("file3.txt","r",encoding="utf-8") as fin:
    for line in fin:
        line=line[:-1]
        name,hobbies=line.split(" ")
        list=hobbies.split("，")
        for sport in list:
            if sport not in sports:
                sports[sport]=1
            else:
                sports[sport]+=1
    print(sports)
    sports=sorted(sports.items(),key=lambda x:x[1],reverse=True)        #x相当于列表中的每一个元组（键值对），而key则是排序的参考对象，即元组的第一号元素
    print(sports)
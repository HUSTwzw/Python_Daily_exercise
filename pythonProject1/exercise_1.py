#①复杂列表特定属性的排序
students=[
         {"ID":201,"name":"Lucy","age":19},
         {"ID":202,"name":"Jack","age":18},
         {"ID":303,"name":"Mack","age":20},
         {"ID":301,"name":"Amy","age":19}
        ]
student=sorted(students,key=lambda x:x["age"],reverse=True)
for stu in student[0:4]:
    print(stu)
print("\n")
student=sorted(students,key=lambda x:x["age"],reverse=False)#事实上x对应列表中的元素（一个个字典），返回"age"对应的value给key
for stu in student[0:4]:
    print(stu)
print("\n")
student=sorted(students,key=lambda x:x["name"],reverse=True)
for stu in student[0:4]:
    print(stu)
print("\n")
student=sorted(students,key=lambda x:x["name"],reverse=False)
for stu in student[0:4]:
    print(stu)
print("\n")
student=sorted(students,key=lambda x:x["ID"],reverse=True)
for stu in student[0:4]:
    print(stu)
print("\n")
student=sorted(students,key=lambda x:x["ID"],reverse=False)
for stu in student[0:4]:
    print(stu)
print("\n")


# 补充:
# lambda()函数:lambda arguments:expression
#lambda是 Python 的关键字，用于定义 lambda 函数.    arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定.   expression 是一个表达式，用于计算并返回函数的结果.
#例子:
"""
num=lambda x:x+2
print(num(6))--->8
"""
# map()函数:map(function, iterable)
#第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
#例子1:map(square,[1,2,3,4])--->[1,4,9,16]
#例子2:map(lambda x:x+1,[1,2,3,4])--->[2,3,4,5]
# reduce()函数:reduce(function,[参数1,参数2,其余参数])
#函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
#例子1:reduce(add,[1,2,3,4])--->10 (先进行1+2=3，再进行3+3=6，最后进行6+4=10)
#例子2:reduce(lambda x,y:x+y,[1,2,3,4])--->10
# filter()函数:filter(function,iterable)
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
#例子:
"""
def is_odd(number):
    if number%2==0:
        return False
    else:
        return True
final_list=filter(is_odd,[1,2,3,4,5,6,7,8,9])--->final_list=[1,3,5,7,9]
"""


#②填写、读取、排序文件
from pathlib import Path
import json
def input_information(path):
    str=""
    flag=0
    for num in range(1,5):
        name=input("tell me name")
        grade=input("tell me grade")
        str+=f"{name}  "
        if flag==3:
            str+=f"{grade}"
        else:
            str+=f"{grade}  "
        flag+=1
    str=json.dumps(str)
    path.write_text(str)

filename1="write.json"
path=Path(filename1)
input_information(path)
try:
    path=Path(filename1)
except FileNotFoundError:
    print("sorry,we failed to find your file")
else:
    content=path.read_text()
    content=json.loads(content)
    content=content.split("  ")
    student={}
    for number in range(1,len(content),2):

        student[content[number-1]]=content[number]

    students=[]
    for number in range(1,len(content),2):
        students.append([content[number-1],int(content[number])])
    sequence=sorted(students,key=lambda x:x[1],reverse=True)

path2=Path("new_write.json")
sequence=json.dumps(sequence)
path2.write_text(sequence)
#备注:path.write_text的功能不够强大，需要使用文件读写操作弥补
# 1.进行DNA(AGCT)排序,输入长度，给出所有组合


#解法1：递归调用函数
bio=["A","G","C","T"]
bio_list=[]
def circle(length,str):
    if length>1:
        for letter in bio:
            str+=letter
            circle(length-1,str)
            str=str[:-1]
    if length==1:
        for letter in bio:
            str+=letter 
            bio_list.append(str)
            str=str[:-1]     

def output():
    length=input("请输入特定长度(1-8)")
    length=int(length)
    circle(length,"")
    print(bio_list)
    print(f"共{len(bio_list)}种组合")

output()


# 解法2:可以发现，长度为n的排列是在长度为n-1的排列的基础上分别加上"A"、"T"、"C"、"G"得到的结果
# 解法2之第一种写法(思路简单，代码不够灵活)：
bio=["A","T","C","G"]
bio_list=[]
temp_list=[""]
temp_copy_list=[]

import copy

def circle1(length):
    for num in range(1,length+1):
        temp_copy_list=copy.deepcopy(temp_list)
        for temp in temp_copy_list:
            for letter in bio:
                temp+=letter
                if len(temp)==length:
                    bio_list.append(temp)
                else:    
                    temp_list.append(temp)
                temp=temp[:-1]

def output():
    length=input("请输入特定长度(1-8)")
    length=int(length)
    circle1(length)
    print(bio_list)
    print(f"共{len(bio_list)}种组合")

output()


# 解法2之第二种写法(算法设计更加精妙)
bio_list=[""]
bio=["A","T","C","G"]
temp_copy_list=[]

def circle2(length):
    global bio_list     #在函数中对bio_list进行了重新赋值(bio_list=[])，因此被视为局部变量，因此需要在函数中使用global声明为全局变量
    for num in range(1,length+1):
        temp_copy_list=copy.deepcopy(bio_list)
        bio_list=[]
        for temp in temp_copy_list:
            for letter in bio:
                temp+=letter
                bio_list.append(temp)
                temp=temp[:-1]

def output():
    length=input("请输入特定长度(1-8)")
    length=int(length)
    circle2(length)
    print(bio_list)
    print(f"共{len(bio_list)}种组合")

output()
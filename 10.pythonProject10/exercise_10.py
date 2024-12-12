# 1.求符合条件的n阶水仙花数


def check(num,n):
    num=str(num)
    num=list(num)
    sum=0
    for number in num:
        number=int(number)
        sum+=number**n
    if sum==int("".join(num)):
        return True,sum
    else:
        return False,sum

n=input("请输入水仙花数的阶数")
n=int(n)
for i in range(10**(n-1),10**n-1):
    status,sum=check(i,n)
    if status:
        print("水仙花数是{}".format(sum))


# 2.随即生成随机个人数(3000-6000)的考试分数(300-750)，根据录取率确定分数线，或者根据录取率确定分数线


import random
list=[]
num=0
flag=True
def auto_generate_score():
    global list
    global num
    num=random.randint(3000,6000)
    for i in range(1,num+1):
        score=random.randint(300,750)
        list.append(score)


def generate_rate(boundary_score):
    global list
    list=sorted(list)
    amount=0
    for single_score in list:
        if single_score >=boundary_score:
            amount+=1
        else:
            continue
    rate=round(amount/num,5)
    rate=rate*100
    return rate


def generate_boundary_score(rate):
    global list
    global num
    position=int(num*rate)
    list=sorted(list,reverse=True)
    score=list[position]
    return score
    

def select():
    global list
    global num
    option=input("选项:1.生成录取率 2.生成录取分数线 3.quit     ")
    if option=="1":
        auto_generate_score()
        boundary=input("请输入录取分数线")
        boundary=int(boundary)
        rate=generate_rate(boundary)
        rate=round(rate,3)
        print(f"录取率为{rate}%")
        list=[]
        num=0

    if option=="2":
        auto_generate_score()
        rate=input("请输入录取率")
        rate=float(rate)
        score=generate_boundary_score(rate)
        print(f"录取分数线为{score}")
        list=[]
        num=0

    if option=="quit":
        global flag
        flag=False


while flag:
    select()
# 1.猜数字游戏：自动生成n位数，用户输入猜测结果，根据输入结果返回xTyF的格式，表示对应位置有x个数字正确，y个数字错误
#   例如：生成的数为490时，用户输入094返回0T3F，输入398返回1T2F，输入491返回2T1F，输入490返回3T0F


def menu():
    option=input("请输入难度等级(quit退出)")
    if option.isdigit():
        option=int(option)
        if option>=1:
            number=generate_number(option)
            return True,number
        else:
            print("输入必须是正整数")
            return True,None
    elif option=="quit":
        return False,None
    else:
        print("输入错误，请重新输入")
        return True,None
        
        
import random
def generate_number(option):
    number=random.randint(10**(option-1),10**option)
    return number


def judge(number):
    num=input("请输入数字(quit退出)")
    if num=="quit":
        return False
    elif num.isdigit():
        num=int(num)
        if num>=1:
            num=str(num)
            flag2=back(number,num)
            return flag2
        else:
            print("数字必须是正整数")
            return True
    else:
        print("输入错误")
        return True    
    
    
def back(number,num):
    if len(number)!=len(num):
        print("输入的数字长度不正确")
        return True
    else:
        t=0
        f=0
        number_list=[i for i in number]
        num_list=[i for i in num]
        for i in range(len(number_list)):
            if number_list[i]==num_list[i]:
                t+=1
        print("{}T{}F".format(t,len(number_list)-t))
        if t==len(num):
            print("答案是{}".format(number))
            return False
        else:
            return True
    
    
flag=True    
while flag:
    flag,number=menu()
    if number!=None:
        flag2=True
        while(flag2):
            flag2=judge(str(number))
# 1.进行1-n报数游戏，报数为n的学生退出，获取最后一人的号码


def find_last(student,number):
    if number<=0 or student<=0:
        print("输入的数值错误")
        return False
    elif number==1:
        print("最后一人是{}号".format(student))
        return False
    else:
        stu_list=[i for i in range(1,student+1)]
        num=0
        while(len(stu_list)>1):
            stu_list_extra=[i for i in stu_list]
            for i in stu_list_extra:
                num+=1
                if num==number:
                    num=0
                    stu_list.remove(i)
                    print("淘汰过程为{}".format(stu_list))
        return stu_list[0]        
            

def menu():
    command=input("输入y进行测试,输入quit退出测试")
    if command=="y":
        student=input("请输入学生的个数")
        if student.isdigit():
            number=input("请输入n")
            if number.isdigit():
                stu_list=find_last(int(student),int(number))
                if stu_list==False:
                    pass
                else:
                    print("最后一位是{}号".format(stu_list))
                    return True
            else:
                print("输入的n不是数字")
                return False
        else:
            print("输入的学生个数不是数字")
            return False
    elif command=="quit":
        print("即将退出")
        return False
    else:
        print("输入错误，请重新输入")
        return True


flag=True
while flag:
    flag=menu()
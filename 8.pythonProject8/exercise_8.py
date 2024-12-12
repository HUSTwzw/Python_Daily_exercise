# 1.改进exercise_7.py，使功能更加完善(增加互动功能),使效果更加真实


from time import sleep
def menue(command):
    if command=="auto":
        auto_generate()
        return 1
    elif command=="manual":
        print("加载成功")
        str=input("请输入字符串")
        manual_check(str)
        return 1
    elif command=="quit":
        return 0
    else:
        print("输入错误，清重新输入")
        return 1


def manual_check(str):
    print("正在判断中……")
    sleep(1)
    if str==str[::-1]:
        print("是回文字符串")
    else:
        print("不是回文字符串")


def auto_generate():
    import random
    letter_range="abcdefg"
    list=random.choices(letter_range,k=random.randint(5,8))
    str="".join(list)
    check=random.randint(0,1)
    if check==0:
        str=str+str[::-1]
    elif check==1:
        str=str+str[-2::-1]
    print("正在自动生成回文字符串……")
    sleep(1)
    print(f"成功生成字符串：{str}")


while True:
    option=input("1.手动输入(manual) 2.自动生成(auto) 3.退出(quit)")
    print("正在加载中……")
    sleep(1)
    outcome=menue(option)
    if outcome==0:
        print("退出程序")
        break
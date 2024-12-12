# 1.随即生成一串字符串，找出最长的回文字符串，若有多个长度相同的最长回文字符串，则一次性都显示出来


import random
def random_str():
    key="abcdefg"
    str=random.choices(key,k=random.randint(10,20))
    return str


def huiwen_str(str):
    str_list=""
    str_len=0
    for i in range(0,len(str)):
        for j in range(i,len(str)):
            string=str[i:j+1]
            if string[::-1]==string:
                if(len(string))>str_len:
                   str_list=string
                   str_len=len(string)
                elif(len(string))==str_len:
                    str_list+=f" {string}"
            else:
                continue
    return str_list               


from time import sleep
while True:
    num=input("请问产生字符串个数")
    if num.isdigit():
        for n in range(1,int(num)+1):
            str=random_str()
            str="".join(str)
            str_list=huiwen_str(str)
            print(f"原字符串是{str}")
            sleep(1)
            print(f"回文字符串是{str_list}")
            sleep(1)
    elif num=="quit":
        break
    else:
        print("输入错误，清重新输入")


# 补充：
# 1."str".join(list):将列表元素以给定字符连接，并以字符串形式返回整合之后的列表
# 例子：
# 1.words="".join(["hello","world","!"])--->words="helloworld!"
# 2.words="*".join(["hello","world","!"])--->words="hello*world*!"
# 注意：words为字符串类型

# 2.str[::-1]表示对字符串从后向前切片，且类型仍为字符串，而str[-1:-5:-1]表示从倒数第一个为起点，倒数第五个为终点(不包含倒数第五个)，进行逆序切片

# 3.random模块：
# random.randint(1,5)表示随机生成一个1-5的整形数字
# random.choices("abcdef",k)表示从"abcdef"中选k个字符(可重复)，以每一个字符为元素，形成一个列表(事实上随机选取的对象也可以是列表)
#①打印当前时间
import datetime
current_time=datetime.datetime.now()        #注意：返回的类型是class(可以通过print(type(变量名)))查看变量类型
print(current_time,type(current_time))
year=current_time.year      #注意：此类型为字符串
month=current_time.month
day=current_time.day
hour=current_time.hour
minute=current_time.minute
second=current_time.second
print(f"{year}年{month}月{day}日{hour}时{minute}分{second}秒")


#②判断字符串是否是正确的日期格式(正则表达式)
import re
date1="2006-8-2"
date2="2006-08-02"
date3="20060802"
def right_date(date):
    if re.match("[\\d]{4}[-][\\d]{2}[-][\\d]{2}",date)==None:
        print("格式错误")
    else:
        print("格式正确")
right_date(date1)
right_date(date2)
right_date(date3)


#补充：
#re.match(pattern,str)函数尝试从字符串开头进行模式匹配，若失败则返回None


#③提取正确的网址
import re
with open("file1.txt","r",encoding="utf-8") as fin:
    content=fin.read()
    pattern=re.compile(r"[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,4}",re.M)
    list=pattern.findall(content)
    print(list)


#补充：
#设置pattern时必须确保字符集后面有+，否则只会从字符集区取一个字符，导致错误
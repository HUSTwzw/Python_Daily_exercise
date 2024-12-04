#①：检验输入的密码是否符合标准格式
#标准格式：6-20位，至少包含小写字母、大写字母、数字、特殊符号各一个
import re
def check(passwords):
    if len(passwords)<6 or len(passwords)>20:
        return "密码长度错误，必须为6-20位"
    elif not re.findall(r"[0-9]",passwords):
        return "密码必须包含数字"
    elif not re.findall(r"[A-Z]",passwords):
        return "密码必须包含大写字母"
    elif not re.findall(r"[a-z]",passwords):
        return "密码必须包含小写字母"
    elif not re.findall(r"[^a-zA-Z0-9]",passwords):
        return "密码必须包含特殊字符"
    else:
        return "密码符合标准"
print(check("hello_world1234"))
print(check("hello_WORLD1234"))
print(check("hello"))
print(check("HELLO1234"))
print(check("U202413490@3056322868@qq.com"))


#②整理购物信息，制作成一个列表
shopping_list=[]
import re
with open("file1.txt","r",encoding="utf-8") as f1:
    for line in f1:

        str=re.search(r"买([0-9]+\.?[0-9]*斤)(.*)，花了([0-9]+\.?[0-9]*元)",line)
        if str==None:
            continue
        else:
            shopping_list.append(str.groups())
    print(shopping_list)


#③对手机号进行加密处理
import re
tel_list=[]
with open("file2.txt","r",encoding="utf-8") as f2:
    for line in f2:
        num=re.findall(r"1[3-9][0-9]{9}",line)
        if len(num)==0:
            continue
        else:
            for list in num:
                list=re.sub(r"(1[3-9])[0-9]{9}",r"\1******",list)
                tel_list.append(list)
    print(tel_list)


#注意：正则表达式的()用于分组，可能造成意想不到的效果，例如num=re.findall(r"(1[3-9])[0-9]{9}")只返回1[3-9]给变量num
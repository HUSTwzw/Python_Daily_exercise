# 1.实现字符串的压缩：
# aaabbbbbcdddd--->3a5bc4d
# 注意：字符串的压缩是为了缩短字符串，因此aaabbbbbcdddd没必要写成3a5b1c4d
def compress(str):
    dictionary={}
    str=list(str)    
    for letter in str:
        if letter not in dictionary:
            dictionary[letter]=1
        else:
            dictionary[letter]+=1
    new_str=""
    for keys,values in dictionary.items():
        if(values==1):
            new_str+=keys
        else:
            new_str+=f"{values}{keys}"
    return new_str
    
str=input("请输入字符串")
new_str=compress(str)
print(new_str)




# 2.实现字符串解压缩：
# 3a5bc4d--->aaabbbbbcdddd
import re
def dis_compress(str):
    pattern=re.compile(r"[0-9]{0,}[a-z]{1}")
    list=pattern.findall(str)
    new_str=""
    for letter in list:
        if(len(letter)==1):
            new_str+=letter
        else:
            match_result=re.search(r"([0-9]+)([a-z])",letter)
            str_num=match_result.group(1)
            str_letter=match_result.group(2)
            num=int(str_num)
            for number in range(1,num+1):
                new_str+=str_letter
    return new_str

str=input("请输入压缩后的字符串")
new_str=dis_compress(str)
print(new_str)
# 1.鸡兔同笼问题改良版(包含对错误数据的反馈)


def trueorfalse(all_head,all_foot):
    if (all_head.isdigit()) and (all_foot.isdigit()):
        all_head=int(all_head)
        all_foot=int(all_foot)
        if all_head<=0 or all_foot<=0:
            print("头和腿的数量必须为正数")
            return True
        elif 2*all_head>all_foot:
            print("头的数量太多了")     
            return True       
        else:
            flag,rabbit_amount,chicken_amount=animal_amount(all_head,all_foot)
            if flag==False:
                print("输入的头与腿数量不匹配")
                return True
            else:
                rabbit_amount=int(rabbit_amount)
                chicken_amount=int(chicken_amount)
                print("兔子数量为{},鸡的数量为{}".format(rabbit_amount,chicken_amount))
                return True
    elif all_head=="quit" or all_foot=="quit":
        print("成功退出")
        return False
    else:    
        print("输入的不是数字")
        return True


def animal_amount(all_head,all_foot):
    rabbit_foot=all_foot-2*all_head
    rabbit_amount=rabbit_foot/2.0
    if rabbit_amount==round(rabbit_amount,0):
        chicken_amount=all_head-rabbit_amount
        if chicken_amount==round(chicken_amount,0):
            chicken_amount=round(chicken_amount,0)
            return True,rabbit_amount,chicken_amount
        else:
            return False,None,None
    else:
        return False,None,None
        

while(True):    
    all_head=input("请输入头的数量：")
    all_foot=input("请输入腿的数量：")
    flag=trueorfalse(all_head,all_foot)
    if flag==False:
        break
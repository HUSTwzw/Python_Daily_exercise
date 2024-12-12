# 1.递归买汽水，1元买1瓶汽水，2个空瓶子换1瓶汽水，3个瓶盖换1瓶汽水，请问最多能喝几瓶汽水


water=0
bottle=0
cap=0

def bottle_water():
    global water 
    global bottle
    global cap
    if bottle>=2:
        bottle=bottle-2
        water=water+1
        bottle=bottle+1
        cap=cap+1
        bottle_water()
    else:
        pass

def cap_water():
    global water
    global bottle
    global cap
    if cap>=3:
        cap=cap-3
        water=water+1
        bottle=bottle+1
        cap=cap+1
        cap_water()
    else:
        pass
    
def amount_init(money):
    global water
    global bottle
    global cap
    water=money
    bottle=money
    cap=money
    
def output():
    global water
    global bottle
    global cap
    print("最多可以买{}瓶水,还剩下{}个瓶子和{}个瓶盖".format(water,bottle,cap))
    
    
while True:   
    money=input("请输入钱(输入quit将退出此程序)")
    if money.isdigit():
    
        money=int(money)
        amount_init(money)
        while(bottle>=2 or cap>=3):
            bottle_water()
            cap_water()
        output()
    elif money=="quit":
        print("即将退出")
        break
    else:
        print("输入错误,请重新输入")
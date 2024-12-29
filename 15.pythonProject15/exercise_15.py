# 1.汉诺塔问题(参用递归的方法)：
"""
  在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)
  移动圆盘时受到以下限制:
  (1) 每次只能移动一个盘子;
  (2) 盘子只能从柱子顶端滑出移到下一根柱子;
  (3) 盘子只能叠在比它大的盘子上。
  请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。
"""

def hannoi(n,origin_site,assisted_site,target_site):
    if (n==1):
        print(f"{origin_site}->{target_site}")
    else:
        hannoi(n-1,origin_site,target_site,assisted_site)
        print(f"{origin_site}->{target_site}")
        hannoi(n-1,assisted_site,origin_site,target_site)

n=input("请输入罗盘数量")
hannoi(int(n),"A","C","B")        

def hannoi(n,origin,assisted,target):
  if n==1:
    target.append(origin.pop())
    
  else:
    hannoi(n-1,origin,target,assisted)
    target.append(origin.pop())
    hannoi(n-1,assisted,origin,target)


A=[4,3,2,1]
B=[]
C=[]
hannoi(4,A,B,C)
print(A,B,C)

"""
n = 1 时,直接把盘子从A移到C
n > 1 时,
    先把上面n-1个盘子从A移到B(子问题,递归)
    再将最大的盘子从A移到C
    再将B上n-1个盘子从B移到C(子问题,递归)
"""
"""
理解递归：
递归函数重在表达前后关系
同时要明确递归结束的条件
"""
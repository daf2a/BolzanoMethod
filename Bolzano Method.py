import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate

x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

print("\n=== Bolzano Method ===\n")

iterate = int(input("Number of Iteration\t\t: "))
lower_x = int(input("Initial lower x\t\t\t: "))
upper_x = int(input("Initial upper x\t\t\t: "))
degree = int(input("Highest Degree\t\t\t: "))

i=degree
koefisien = []
iterate2=iterate

while i >= 0 :
    string="Coefficient number of x^" + str(degree-i) + "\t: "
    koefisien.append(int(input(string)))
    i -= 1

x4=np.linspace(lower_x, upper_x,100)
y4=[]

k=0
while k!=100:

    res = 0
    i=degree   
    while i>=0 :
        temp = abs(math.pow(x4[k], i))*int(koefisien[i])
        res+=temp
        i-=1
    y4.append(res)
    k+=1

plt.plot(x4,y4,color='green')

temp=0
while iterate >0 :

    res = 0
    i=degree   
    while i>=0 :
        temp = abs(math.pow(lower_x, i))*int(koefisien[i])
        res+=temp
        i-=1
    y1_temp=res

    res = 0
    i=degree    
    while i>=0 :
        temp = abs(math.pow(upper_x, i))*int(koefisien[i])
        res+=temp
        i-=1
    y2_temp=res

    x3_temp=(lower_x+upper_x)/2
    res = 0
    i=degree    
    while i>=0 :
        temp = abs(math.pow(x3_temp, i))*int(koefisien[i])
        res+=temp
        i-=1
    y3_temp=res
    
    x1.append(lower_x)
    x2.append(upper_x)
    x3.append(x3_temp)

    y1.append(y1_temp)
    y2.append(y2_temp)
    y3.append(y3_temp)

    if(y3_temp<0):
        lower_x=x3_temp
    if(y3_temp>0):
        upper_x=x3_temp
    
    iterate-=1

NumIterate=[]
j=1
while j<=iterate2 :
    NumIterate.append(j)
    j+=1

data = {
    'No' :  NumIterate,
    'x1' : x1,
    'x2' : x2,
    'x3' : x3,
    'f(x1)' : y1,
    'f(x2)' : y2,
    'f(x3)' :y3
}

print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

plt.grid()
plt.title("Bolzano Method")

plt.scatter(x3, y3,color='blue')
plt.scatter(x3[iterate2-1], y3[iterate2-1], color='red')
plt.show()







# coding: utf-8

# In[2]:


from math import exp
import numpy as np
import numpy 
import pandas as pd
from matplotlib import pyplot as plt
import operator
import random
whitecells=[]
blackcells=[]
dt=pd.read_csv('local1.csv',sep=',',encoding='cp1252')
arr=dt.values
y =np.array(arr)
t=[]
tot=0
i=0
j=0
for i in range(37):
    for j in range(37):
        if y[i][j]!="G":
            t.append(int(y[i][j]))
        else:
            t.append(y[i][j])
ad=np.array(t)
nd=np.reshape(np.ravel(ad), (37, 37))
total=0
x=0
y=0
k=[]
ty=[]
c=0
dict1={}
dict2={}
mt=np.array(nd)
nt=np.array(nd)     ##main matrix   
                     ##probability matrix
def neigh(x,y):
    if x < (len(nd)-1):
            k.append((x+1,y))        
    if y >0:
            k.append((x-1,y))
    if x<(len(nd)- 1):
            k.append((x,y+1))

    if y>0:
            k.append((x,y-1))
    return k
def formdictionary(k):          
    i=0
    while(i<len(k)):       ## k consisit of co-ordinates neighbours
        t,p=k[i]
        val=nt.item(t,p)  ##value of the matrix
        dict2={(t,p):val}##value of cells and co-ordinates
        dict1.update(dict2)
        i=i+1    
    return dict1
##count zero's and G
i=0
j=0
for i in range(37):
    for j in range(37):
        if mt.item(i,j)=="G" or int(mt.item(i,j))==0:
            c=c+1


###probability matrix
prob=float(1/(c))

for i in range(37):
    for j in range(37):
        if mt.item(i,j)=="G" or int(mt.item(i,j))==0:
            nt[i,j]=prob


##traversing
def calculateprob(f,g,prob,total):
    total=total+1
    nt[f,g]=-5
    mt[f,g]=-5
    k=neigh(f,g)
    dictio=formdictionary(k)
    sorted_x = sorted(dictio.items(), key=operator.itemgetter(1),reverse=True)    
    x1,x2=sorted_x[0][0]
    val=sorted_x[0][1]
    count=0
    for i in range(37):
        for j in range(37):
            if mt.item(i,j)=="G" or int(mt.item(i,j))==0:
                count=count+1
    updaprob=float(val)/(count)
    prob=prob+updaprob
    
    for i in range(37):
        for j in range(37):
            if mt.item(i,j)=="G" or int(mt.item(i,j))==0:
                nt[i,j]=prob
    if mt.item(x1,x2)=="G":
        print("found")
        print(total)
    else:
        calculateprob(x1,x2,prob,total)

for i in range(37):
        for j in range(37):
            if mt.item(i,j)=="G" or int(mt.item(i,j))==0:
                whitecells.append((i,j))
            else:
                blackcells.append((i,j))


b,v=(random.choice(whitecells))

print(b,v)
if mt.item(b,v)=="G":
    print("found at 30 30")
else:
    total=calculateprob(b,v,prob,total)










print(np.matrix(mt))
print(np.matrix(nt))  
     
     


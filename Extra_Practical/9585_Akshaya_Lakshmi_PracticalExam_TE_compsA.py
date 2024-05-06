#!/usr/bin/env python
# coding: utf-8

# In[41]:


# dynamic input
def cost(current):
    return 1

def next_moves(current):
    m,c,b=current
    nextmv=[]
    xx=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    for x,y in xx:
        if b==1:
            n=(m-x,c-y,0)
        else:
            n=(m+x,c+y,1)
        if 0<=n[0]<=3 and 0<=n[1]<=3 and (n[0]>=n[1] or n[0]==0) and (3-n[0]>=3-n[1] or 3-n[0]==0):
            nextmv.append(n)
    return nextmv

def ucs(start,goal):
    frontier=[(0,[(start)])]
    visited=set()
    while frontier:
        frontier.sort()
        c,current=frontier.pop(0)
        if current[-1]==goal:
            print("Goal achieved")
            return current
        if current[-1] in visited:
            continue
        visited.add(current[-1])
        p=next_moves(current[-1])
        for nextm in p:
            frontier.append((c+cost(current[-1]),current+[nextm]))
    return None

missionary=int(input("Enter number of missionaries "))
cannibal=int(input("Enter number of cannibals "))
print("boat starts at the left shore by default")
start_g=(missionary,cannibal,1)
end_g=(0,0,0)
solution=ucs(start_g,end_g)
if solution:
    for s in solution:
        print(s) 
else:
    print("No solution")

print("Roll no. 9585")


# In[26]:


#static input
def cost(current):
    return 1

def next_moves(current):
    m,c,b=current
    nextmv=[]
    xx=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    for x,y in xx:
        if b==1:
            n=(m-x,c-y,0)
        else:
            n=(m+x,c+y,1)
        if 0<=n[0]<=3 and 0<=n[1]<=3 and (n[0]>=n[1] or n[0]==0) and (3-n[0]>=3-n[1] or 3-n[0]==0):
            nextmv.append(n)
    return nextmv

def ucs(start,goal):
    frontier=[(0,[(start)])]
    visited=set()
    while frontier:
        frontier.sort()
        c,current=frontier.pop(0)
        if current[-1]==goal:
            print("Goal achieved")
            return current
        if current[-1] in visited:
            continue
        visited.add(current[-1])
        p=next_moves(current[-1])
        for nextm in p:
            frontier.append((c+cost(current[-1]),current+[nextm]))
    return None

start_g=(3,3,1)
end_g=(0,0,0)
solution=ucs(start_g,end_g)
if solution:
    for s in solution:
        print(s) 


# In[ ]:





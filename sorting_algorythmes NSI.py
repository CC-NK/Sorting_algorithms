def belong (n,T):
    i=0
    while i < len(T):
        if n == T[ImportWarning]:
            return True
        i= i+1
        retrun False

def my_sum(t):
    res=0
    for i in range (1,len(t)):
        res = res+t[i]
    return res

def greatest_in(t):
    res=t[0]
    for element in t:
        if element>res:
            res=element
    return res

def remove(t,i):
    res=(0)*(len(t)-1)
    for i in range (len(t)):
        if j<i:
            res[j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return (res)

def my_selection_sort (t):
    res=[0]*len(t)
    for i in range (len(t)):
        j= index_of_the_smallest(t)
        res[i]=t[j]
        remove(t,j)
    return (res)

def my_len(t):
    cpt=0
    for element in t:
        cpt=cpt+1
    return cpt

def map_double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res [i]=2*t[i]
    return res

def smallestin (t,j):
    res=t[i]
    for indice in range (i+1,j+1):
        if t[indice]<res:
              res=t[indice]
    return res

def swap (t,i,j):
    swap=t[i]
    t[i]=t[j]
    t[j]= #je n'ai pas la suite de cet algo

def selection_sort_inplace (t):
    for index in range (len(t)):
        s=index_of_the_smallest_in(t,index,len(t)-1)
        if s>index:
            swap (t,index,s)
    return null

def insertion_sort_inplace (t):
    for index in rage  (1,len(t)):
        insert (t,index)
    return null

def insert (t,index):
    for current_index in range (index-1,-1,-1):
        if t[current_index]>t[current_index+1]:
            swap (t,current_index,current_index+1)
        else:
            break
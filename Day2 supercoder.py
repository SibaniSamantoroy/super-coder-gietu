'''#List>----
List1=[]
print(List1,type(List1))
List2=[10,20,30,40]
print(List2,type(List2))
list3=[10,20.3,30+3j,True,"Python"]
print(list3,type(list3))
list3.append(50)
print(list3,type(list3))
list3.extend([50,56,40])
print(list3,type(list3))
list3.insert(0,57)
print(list3,type(list3))
list3.insert(4,89)
print(list3,type(list3))
list3.remove(56)
print(list3,type(list3))
list3.pop()
print(list3,type(list3))
list3.pop(1)
print(list3,type(list3))
del list3[0]
print(list3,type(list3))



def count_str(s):
    l,d=0,0
    for i in s:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            d+=1
        else:
            pass
    list1=[]
    list1.extend([l,d])
    return list1
             
string=input("enter the string")
print("the string",count_str(string))


def function(n,sum1):
    c=0
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            if(n[i]+n[j]==sum1):
                c+=1
                break
            else:
                continue
    if(c==0):
        return 0
    else:
        return c

n=list(map(int,input().split()))
sum1=int(input())
print(function(n,sum1))


def function(l1):
    if(len(l1)<2):
        return -1
    else:
        return l1[0:2]+l1[-2:]

l1=input()
print(function(l1))

def function(s1):
    s2="ing"
    if(len(s1)<3):
        return s1
    elif(s1[-3:]==s2):
        return s1+"ly"
    else:
        return s1+"ing"

s1=input()
print(function(s1))


def fun(s1):
    double=s1*2
    n1=str(n1)
    double=str(double)
    if(len(s1)==len(double)):
           for i i n1:
           if(i in double and n1.index(i)!=double.index(i):
           
           return True
        else:
            return False
        else:
            return False
n=input()
print(fun(s1))

def find_Average(t1):
    sum1,n=0,0
    for i in t1:
        sum1=sum1+i
        avg=sum1/10
    for i in t1:
        if(i>=avg):
            n+=1
        else:
            per=(n/10)*100
    return per


def freq(t1):
    l1=[]
    for i in range(0,26):
        l1.append(t1.count(i))
    return l1

def sort(t1):
    t2=list(t1)
    t2.sort()
    return t2
t1=input()
print(find_Average(t1))

print(freq(t1))
print(sort(t1))

def translate(dict1,eng):
    l1=[]
    for i in eng:
        l1.append(dict1[i])
    return l1
dict1=["merry":""god","christmas":"jul","and":"och","happy":"gott","year":"ar" ]]
str=input()
print(translate(dict1,eng))'''




n1=int(input("enter a value for n1")
n2=int(input("enter a value for n2")
result=[]
for i in range(n1,n2+1)
       result.append(i)
print(result)
array=[i for i in range(n1,n2+1)
print(array)






    

    




    




    








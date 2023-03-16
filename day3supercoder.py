'''#list comphrehension
#for loop version
result=[]
for i in range(l1):
    result.append(i)
print(result)
#list comphrehension version
print([i for i in range(l1)])
#for loop version......odd elements
result=[]
for i in range(l1):
    if i%2%=0:
        result.append(i)
print(result)
print([i for i in range(l1)if i%2!=0])



result=[]
for i in range(l1):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(l1)])


result[]
for i in range(l1):
    if i%2!=0:
        result.append(i**2)
    else:
        result.append(i**3)
print(result)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print[matrix[i][j]**2 if(matrix[i][j]%2!=0) else matrix[i][j]**3 for i in range(0,len(matrix)) for j in range(0,len(matrix[0]))]


 

result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele %2!=0:
            result.append(i**2)
        else:
            result.append(i**3)


#tuples

mylist = [9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]  

for i in list_b:
    result.append((i,mylist.index(i)))
print(result)


print([i,mylist.index(i) for i in list_b])


sentences = ["a new world record was set","in the holy city of ayodhya ","on the eve of diwali on tuesday","with over 3 lakh diya or earthen lamps","lit up simultaneously on the banks of sarayu river"]
stopwords=['for','a','of','the','and ','to','in','on','with','was']
res=[]
for i in sentences:
    for ch in i.split():
        if ch not in stopwords:
            res.append(ch)
print(res)



#3,2,6,5,1,4,8,9

#num1=3+2+6+9=20
#num2=5148
#o/p=5148+20=5168
string=list(map(int,input().split(",")))
sum1=0
string2=""
for i in range(len(string)):
    if(i<string.index(5) or i>string.index(8)):
        sum1+=string[i]
    else:
        string2+=str(string[i])
print(sum1+int(string2))


#rhdt:246  ,ghftd:1246

#2*2+4*4+6*6=56


string=list(input().split(":"))
sum1=0
str2=" "
for i in string[1]:
    sum1+=int(i)*int(i)
if(sum1%2==0):
    str2+=(str2[-1]+str2[:len(str2)-1])
print(str2)
else:
    str2+=(str2[-3:-1]+str2[-1]+str2[0:len(str2)-3])
print(str2)'''

def check_prime(n):
    





        
        


    





    
    








            
             




            



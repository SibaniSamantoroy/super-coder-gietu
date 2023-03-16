''''#problem1-------
#function nearest palindrome to accpt a number


import sys
def next_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(next_palindrome(99))
print(next_palindrome(101))


#problem2---------
dict1={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
l1=list(map(str,input().split("")))
med1=" "
c=0
for i in d1.keys:
        if(l1.count(i)>c):
             c=l1.count(i)
             med=i
       
        
print(dict1[med])

#problem3
str1="I like Python"
str2="Java is a very popular language"

l3=" "


for i in range (0,len(str1)):
    if(str1[i]!=" "):
        for j in range (0,len(str2)):
            if(str1[i]==str2[j]):
                 l3+=str1[i]
                 break
print(l3)

#oops in python
class employee:
    def_init_(self):
        self.employee_id = None
    def check.eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()


class Example:
    
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())  #10 15



class Customer:
    def __init__(self):
        cust_id=100


c1=Customer()
print(c1.cust_id)  ###error

class Customer:
    def __init__(self,id):
        self.id=100

c1=Customer(200)
print(c1.id)


class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material=material

s1=Shoe(1000,"canvas")
print ("the unique id of the object",id(s1))
print(s1.price,s1.material)


class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__(self):
        return "Shoe with price:" + str(self.price) + " and material:"+ self.material

s1=Shoe(1000,"Canvas")
print(s1)

class Mobile:
    def display(self):
        print (id(self))
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating the price")

Mobile().purchase()
m1=Mobile()
print(m1)


    ###object is initialized
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print(self.total_price)
    
m1=Mobile("Apple",20000)
m1.purchase()



class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.wallet_balance+=amount
    def show_balance(self):
        print("the balance is",self.wallet_balance)
c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()


class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.__name)
print("dam Length",dam1.get_length())'''

class Table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)



        
        
   
          











    

    










        
     

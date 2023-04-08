'''############sorting###########
##########selection sort#######
def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):#to sort in descending order,change > to < in this iteration
            if array[i]<array[min_idx]:#select the minimum element in each loop
                min_idx=i
                #put the min at the correct position
            (array[step],array[min_idx])=(array[min_idx],array[step])
        return array

data=[20,12,10,15,2]
new_data=selectionsort(data,len(data))
print(new_data)



###########################problem1########################################
class fruit_info:
    def __init__(fruit_namelist,fruit_pricelist):
        self.fruit_namelist=fruit_namelist
        self.fruit_pricelist=fruit_pricelist
    def get_fruit_price(fruit_name):
        if(fruit_name in self.fruit_namelist):
            return self.pricelist[self.namelist.index(fruit_name)]
        else:
            return -1

###############################probltm2###############################
class employee:
    def validate_


##############################bakehouse###################################
class Node(self,data):
    self.data=data
    self.next=None

class bakehouse:
    def __init__(self):
        self.__occupied_table_list=[]

    def get occupied_table_list(self):
        return self.__occupied_table_list
    def allocate_table:
        start=self.head
        newnode=
        while(start.next is not None):
            start=start.next
            newnode.next=start.next
            
            

















list1=bakehouse()
list1.head=Table(1)
l2=Table(2)
l3=Table(3)
l4=Table(4)
l5=Table(5)
l6=Table(6)
l7=Table(7)
l8=Table(8)
l9=Table(9)
l10=Table(10)

#linking of table
list1.head.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
l6.next=l7
l7.next=l8
l8.next=l9
l9.next=l10

print("allocate tables are",list1.allocate_table)
print("allocate tables are",list1.allocate_table)


print("allocate tables are",list1.allocate_table)
print("occupied table are:")
list1.deallocate_table()
print("occupied tables")
print(list1.get_occupied_table_list)








########################chocolate#############
def rewardchild(t1,l1,sid,extra_choco):
    index=t1.index(sid)
    l1[index]+=extra_choco
    return l1

def total_chocolate(l1):
    return sum(l1)





child_id=tuple(10,20,30,40,50)
choco_recieved=[1,2,3,4,5,6]
sid=int(input("enter id of the student"))
extra_choco=int(input("enter the extra chocolate")
if(sid not in child_id):
    print("child id is invalid")
elif(extra_choco<1):
    print("extra chocolates is less than 1")
else:
    choco_recieved=reward child(child_id,choco_recieved,sid,extra_choco)
print("total chocolates"totalchcolates(choco_recieved)
print("list of chocolates recieved ",choco_recieved)'''

#####################quick sort##############
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if(array[j]<=pivot):
           i=i+1
           (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

data=[8,7,6,1,0,9,2]
print("unsorted array")
print(data)
size=len(data)
quicksort(data,0,size-1)
print("sorted array in ascending order")
print(data)

#################################
str1=
freq=0

                
                
                
        

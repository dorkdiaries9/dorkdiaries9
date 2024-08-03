class Node:
   def __init__(self,roll,name):
      self.roll=roll
      self.name=name
      self.next=None

   def show(self):
      print(self.roll,self.name,end="->")

class List:
   def __init__(self):
      self.head=None

   def traverse(self):
      current=list.head
      while current is not None:
         current.show()
         current=current.next

i=1
list=List()
while(i<4):
   roll=int(input("Enter Rollno:"))
   name=input("enter name:")
   n1=Node(roll,name)
   if(list.head==None):
      list.head=n1
   else:
      current=list.head
      while current.next is not None:
         current=current.next
      current.next=n1
   i=i+1

print("Data are:")

list.traverse()
 
print(None)

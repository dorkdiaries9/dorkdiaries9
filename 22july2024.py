class Node:
   def __init__(self,data):
      self.data=data
      self.next=None

   def show(self):
      print(self.data,end="->")

class List:
   def __init__(self):
      self.head=None

   def traverse(self):
      current=list.head
      while current is not None:
         current.show()
         current=current.next



   def insertbegin(self):
      current=list.head
      #data=input("enter data to insert in first position of node")
      new_node=Node(90)
      new_node.next=list.head
      list.head=new_node


   def insertmiddle(self,pos,data):
      new_node=Node(data)
      current=list.head
      for i in range(pos-1):
         current=current.next
      new_node.next=current.next
      current.next=new_node
      
   def insertend(self):
      new_node=Node(66)
      current=list.head
      #data=input("enter data to insert in first position of node")
      while current.next is not None:
         current=current.next
         
      current.next=new_node 

   def deletefirst(self):
      if list.head is not None:
         list.head=list.head.next

   def deleteend(self):
      list.current=list.head
      while list.current.next.next is not None:
         list.current=list.current.next

   #def deletemiddle(self):

    
i=1
list=List()
while(i<6):
   d=input("Enter a data:")
   n1=Node(d)
   if(list.head==None):
      list.head=n1
   else:
      current=list.head
      while current.next is not None:
         current=current.next
      current.next=n1
   i=i+1

print("Data are:")

#list.insertbegin()

#list.insertmiddle(3,25)

#list.insertend()

list.deletefirst()

list.deleteend()

list.traverse()
 
print("End")

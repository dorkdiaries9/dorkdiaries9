'''
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
person=Person("Gilbert Blythe",20)
person.age=-5
print("age after invalid set:",person.age)
person.age=25
print("updated age:",person.age)

class Book:
   def __init__(self,name,author):
      self.bookname=name
      self.author=author
      self.status=True

   def showInfo(self):
      print("Author:",self.author,"book title:",self.bookname)

   def getStatus(self):
      return self.status

   def setStatus(self,s):
      self.status=s


class Student:
   def __init__(self,stud_id,name,stud_class):
      self.s_id=stud_id
      self.s_name=name
      self.s_class=stud_class

   def showinfo(self):
      print("student id:",self.s_id,"name:",self.s_name,"class:",self.s_class)

   def issueBook(self,object1):
      if object1.getStatus()==True:
         print("\nBook:",object1.bookname,"by",object1.author,'issused to',self.s_name)
         object1.setStatus(False)
      else:
               
         print("\Book:",object1.bookname,"by",object1.author,"is not available")

   def returnBook(self,object1):
      object1.setStatus(True)
      print("Book:",object1,"returned Successfully.")
     

b1=Book("Harry Potter","J K ROWLING")
b2=Book("golden Roads","Robert willer")
s1=Student(1,'manoj','5th')
s1.issueBook(b1)
s2=Student(2,'Ankit','6th')
s2.issueBook(b1)

'''

class Product:
   def __init__(self,pid,pname,price,stock):
      self.pid=pid
      self.pname=pname
      self.price=price
      self.stock=stock
      self.status=True

   def showInfo(self):
      print("Product:","id:",self.pid,"name",self.pname,"product price:",self.price,"stock",self.stock)

   def getStatus(self):
      return self.status

   def setStatus(self,s):
      self.status=s


class Customer:
   def __init__(self,cid,cname):
      self.cid=cid
      self.cname=cname

   
   def showinfo(self):
      print("customer id:",self.cid,"customer name:",self.cname)   

   def purchase(self,object1):
      if object1.getStatus()==True:
         upstock=self.stock-1
         print("\nProduct:",object1.pname,"product id",object1.pid,'purchased by',self.cname,"stock",upstock)
         object1.setStock(False)

      #if stock==0:
         print("\nProduct:",object1.pname,"product id",object1.pid,"is not available")
      else:
         print("thank you")

p1=Product("101","bottle","250",50)
p2=Product("102","book","500",10)
p3=Product("103","pen","50",100)

c1=Customer(1,'anne')
c1.purchase(p1)

c2=Customer(2,'amit')
c2.purchase(p1)

c3=Customer(3,'sujal')
c3.purchase(p3)  


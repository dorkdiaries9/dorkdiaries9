'''
class student:
   def __init__(self):
     
      self.roll=int(input("enter roll no:"))
      self.name=input("enter name:")
      self.std=input("enter student class:")
      self.mrks1=int(input("enter marks in Python:"))
      self.mrks2=int(input("enter marks in Java:"))
      self.mrks3=int(input("enter marks in Algorithms:"))

   def total(self):
      self.tot= self.mrks1+self.mrks2+self.mrks3
      print("total marks =",self.tot)

   def percentage(self):
      self.per=self.tot/300*100
      print("Percentage =",self.per)

o1=student()
o1.total()
o1.percentage()


o2=student()
o2.total()
o2.percentage()

o3=student()
o3.total()
o3.percentage()


class student:
   def __init__(self):
      self.roll=roll
      self.name=name
      self.std=std
      self.mrks1=mrks1
      self.mrks2=mrks2
      self.mrks3=mrks3
     
      

   def total(self):
      self.tot= self.mrks1+self.mrks2+self.mrks3
      print("total marks =",self.tot)

   def percentage(self):
      self.per=self.tot/300*100
      print("Percentage =",self.per)

for i in range(3):      
   roll=int(input("enter roll no:"))
   name=input("enter name:")
   std=input("enter student class:")
   mrks1=int(input("enter marks in Python:"))
   mrks2=int(input("enter marks in Java:"))
   mrks3=int(input("enter marks in Algorithms:"))


   o1=student()
   o1.total()
   o1.percentage()

'''
class student :

   def __init__(self):
      self.roll=roll
      self.name=name
      self.std=std
      self.s1=s1
      self.s2=s2
      self.s3=s3

   def total(self):
      self.tot=self.s1+self.s2+self.s3
      print("total",self.tot)

   def per(self):
      self.p=self.tot/300*100
      print("per",self.p)

for i in range(3):
   roll= int(input("roll:"))
   name= (input("name:"))
   std= (input("class:"))
   s1= int(input("html:"))
   s2= int(input("java:"))
   s3= int(input("python:"))


   s=student()
   s.total()
   s.per()


import math
import random
from typing import AsyncGenerator

# print(math.sqrt(31))
# print(math.fabs(-5))
# print(math.floor(4.6))
# print(math.ceil(4.6))
# print(math.pow(2,2))
# print(math.trunc(7.999))


# print(math.sin(0))
# print(math.sin(3))
# print(math.tan(3))
# print(math.cos(3))


# print(math.pi)
# print(math.tau)
# print(math.e)
# print('positive infinity- ',math.inf)
# print('negative infinity- ',-math.inf)


# radius=int(input('enter circle radius: '))
# area=math.pi*radius*radius
# print('area of circle with a radius of ',radius,' is:',area)

# print(random.random())
# print(random.randint(1,100))
# print(random.randrange(51,100))
# print(random.randrange(0,100,5))

print('the dice rolled',random.randint(1,6),'and',random.randint(1,6))

# dice=int(input('number of dice: '))
# sides=int(input('number of die sides: '))
# die=0
# while die < dice:
#     print('die =',random.randint(1,sides))
#     die=die+1



# name=input('enter name: ')
# age=input('enter age: ')
# print(('Hello, {}. You are {} years old').format(name,age))
# print(('Hello, {}. You are {} years old').format('Bruce',57))

# guess=int(random.randint(1,10))
# num11=int(0)
# while num11 != guess:
#     num11 = int(input("enter guess between 1 and 10: "))
#     if num11==guess:
#         print("Great guess!!!")
#     else:
#         print("Try again")

# days={'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
# for day in days:
    # print(day)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a|b) #alternately print(a.union(b))
# print(a&b) #alternately print(a.intersection(b))
# print('a-b=',a-b) #alternately print('a-b=',a.difference(b))
# print('b-a=',b-a) #alternately print('b-a=',b.difference(a))
# print(sum(b))
# print(max(a))
# print(len(a))
# print(sorted(days))

# print(a)
# a.pop()
# print(a)

# a.discard(6) # this will run and not give a code error even though 6 is not part of set a
# print(a)
# a.remove(6) # this returns a code error since 6 is not part of set a
# print(a)

# class Employee:
#     totalEmployees=0
    
#     def __init__(self,empName,age,designation,salary):
#         self.empName=empName
#         self.age=age
#         self.designation=designation
#         self.salary=salary
#         Employee.totalEmployees=Employee.totalEmployees+1

#     def getEmpDetails(self):
#         return self.empName,self.age, self.designation,self.salary

#     def updateSalary(self,newSalary):
#         self.salary=newSalary
#         print('Salary Updates')
#         return self.salary

# empOne=Employee('John',35,'Manager',35000)
# print(empOne.getEmpDetails())
# empTwo=Employee('Sam',26,'Python Programmer',27000)
# print(empTwo.getEmpDetails())
# empOne.updateSalary(40000)
# print(empOne.getEmpDetails())
# print(Employee.totalEmployees)

# class Intern(Employee):
#     def __init__(self,empName,age,designation,salary,internPeriod):
#         self.internPeriod=internPeriod
#         Employee.__init__(self,empName,age,designation,salary)
#     def getPeriod(self):
#         return 'Internship period (in months) is', self.internPeriod

# internOne=Intern('Tom',22,'Marketing Intern',12000,6)
# print(internOne.getEmpDetails())
# print(internOne.getPeriod())
# print(Employee.totalEmployees)


# threading lesson 19

# from threading import *
# import threading
# from time import sleep

# lock=threading.Lock()
# class Example(Thread):
#     def run(self):
#         for _ in range(5):
#             lock.acquire()
#             print('lock acquired')
#             print('Hello from Example')
#             sleep(0.2)
#             lock.release()

# class ExampleTwo(Thread):
#     def run(self):
#         for _ in range(5):
#             lock.acquire()
#             print('lock acquired')
#             print('Hello from ExampleTwo')
#             sleep(0.2)
#             lock.release()

# example=Example()
# exampleTwo=ExampleTwo()
# example.start()
# sleep(0.1)
# exampleTwo.start()
# example.join()
# exampleTwo.join()
# print('end of program')


# lesson 20 library management app

# Lesson 21 MySQL database connectivity

# import mysql.connector
# myDB=mysql.connector.connect(host="localhost",user="root",passwd="Lagnaf31",database="pythonx")
# myCur=myDB.cursor()
# myCur.execute("select * from user")
# result=myCur.fetchall()
# for i in result:
#     print(i)
# myDB.close()

# Lesson 22 GUI (tkinter)

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def greetUser(event):
    username=inputBox.get()
    greet['text']='Welcome ' + username

window=Tk()
name=Label(window,text='PythonX - Learn Python',bg='white',fg='blue',font=('serif',16))
img=Image.open('Bumble.png')
logo=ImageTk.PhotoImage(img)
image=Label(window,image=logo)

frame=Frame(window)
username=Label(frame,text='UserName',font=('serif',12))
inputBox=Entry(frame)
button=Button(window,text="Let's Start")
button.bind('<Button-1>',greetUser)
greet=Label(window)

name.pack()
image.pack()
frame.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.pack()
window.mainloop()

# def showMessage():
#     messagebox.showinfo('PythonX - Learn Python','Welcome')

# if __name__=='__main__':
#     gui()



# button.place(x=230,y=600)

# window=Tk()
# lbl=Label(window,text='Choose your one favorite programming language')
# # btn=Button(frame,text='Inside the frame')
# # frame=Frame(window)
# var=StringVar()
# python=Radiobutton(window, text='Python', variable=var, value='Python')
# java=Radiobutton(window, text='Java', variable=var, value='Java')
# js=Radiobutton(window, text='JavaScript', variable=var, value='JavaScript')
# cpp=Radiobutton(window, text='C++', variable=var, value='C++')
# var.set('none')  # sets the default to have all of the radio buttons off

# lbl.pack()
# # frame.pack()
# python.pack()
# java.pack()
# js.pack()
# cpp.pack()

# lbl.pack(side=TOP)
# btn.pack(side=BOTTOM)

# window.mainloop()

#!/usr/bin/env python
# coding: utf-8

# In[14]:


#FAULTY CALCULATOR
#this calculator is designed to operate faulty(or give wrong results) for some inputs and works properly for other values. 
#this is done inorder to prevent the user(mainly students) from cheating in exams!!!
def addi():
    print("Enter two values that you wanna add")
    a =int(input())
    b =int(input())
    if a==1 and b==2:
        c = 21
        return c
    elif a==10 and b==10:
        c = 100
        return c
    elif a==5 and b==5:
        c = 55
        return c
    else:
        c = a + b
        return c
def subi():
    print("Enter two values that you wanna subtract")
    a = int(input())
    b = int(input())
    if a ==5 and b ==5:
        c = 100
        return c
    elif a==1 and b ==1:
        c =2
        return c
    elif a==10 and b ==10:
        c = 1000
        return c
    else:
        c = a-b
        return c
def multi():
    print("Enter two values that you wanna multiply")
    a = int(input())
    b = int(input())
    if a == 1 and b==1:
        c = 11
        return c
    elif a == 100 and b ==2:
        c = 102
        return c
    elif a ==5 and b ==5:
        c = 45
        return c
    else:
        c = a*b
        return c
def divi():
    print("Enter two values that you wanna divide")
    a = int(input())
    b = int(input())
    if a == 1 and b==1:
        c = 0
        return c
    elif a == 5 and b ==5:
        c = 50
        return c
    elif a ==25 and b ==5:
        c = 30
        return c
    else:
        c = a/b
        return c
def perci():
    print("Enter both the percent which you wanna calculate and also the total amount")
    a = int(input("Enter the percent you wanna calculate "))
    b = int(input("Enter the total amount from which you wanna calculate"))
    if a == 10 and b==100:
        c = 0
        return c
    elif a==2 and b==50:
        c = 500
        return c
    else:
        c = (a/100)*b
        return c
    

print("Operations that you can do")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Percentage")
o = int(input("Select the operation"))
if (o==1):
    c =addi()
    print("Your answer is {}".format(c))
elif(o==2):
    c =subi()
    print("Your answer is {}".format(c))
elif(o==3):
    c =multi()
    print("Your answer is {}".format(c))
elif(o==4):
    c = divi()
    print("Your answer is {}".format(c))
elif(o==5):
    c = perci()
    print("Your answer is {}%".format(c))


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Question 1

#  For this challenge create a bankaccount class that has two attributes:
#  OwnerName
#  balance
#  and two methods
#  deposit
#  withdraw
#  As an added requirement,withdrawals may not exceed the available balance
#  instantiate your class make several deposits and withdrawals and test to make sure that the account can't overdrawned

# In[26]:


class BankAccount: 

    def __init__(self): 

        self.ownerName= "NGOZI"
        
        self.Balance=0
        
    def deposit(self): 
        
        Amount=float(input("\nEnter amount to be Deposited : ")) 
        
        self.Balance += Amount 
        
        print("\nAmount Deposited is :",Amount) 
  
    def withdraw(self): 
        
        Amount = float(input("\nEnter amount to be Withdrawn : ")) 
        
        if self.Balance >= Amount: 
        
            self.Balance -= Amount 
            
            print("\nYou have Withdrew :", Amount) 
        
        else: 
        
            print("\nInsufficient balance in the account...") 

print("\n---WELCOME TO BACK ACCOUNT PROGRAM---")
    
BA = BankAccount()

print("\nAccount Holder Name is :",BA.ownerName)
    
print("\nInitial Account Balance is :",BA.Balance)
   
BA.deposit();
    
BA.withdraw();
    
print("\nNet Avaliable balance is : ",BA.Balance)
    


# In[27]:


import math

pi = math.pi

class cone:
    
    def __init__(self,r,h): 

        self.r=r
        
        self.h=h
        
    def volume(self):
        
        result = (1 / 3) * pi * self.r * self.r * self.h
        
        print("\nVolume Of Cone is :",result)
        
    def surfacearea(self):
        
        result = pi * self.r * self.h + pi * self.r * self.r
         
        print("\nSurface Area Of Cone is :",result)
        


# In[29]:


radius = float(input("\nEnter the radius of cone : "))

height = float(input("\nEnter the height of cone : "))

c = cone( radius, height)

c.volume()

c.surfacearea()


# In[ ]:





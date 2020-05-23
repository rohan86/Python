import os


class employee:
    raise_amt = 1.05

    def __init__(self,fn,ln,sal):
     self.fn = fn 
     self.ln = ln
     self.email = fn + '.' + ln + 'gmail.com'
     self.sal = sal
     
    def fullname(self):
        return'{} {}'.format(self.fn,self.ln)
    
    def salraise(self):
        self.sal = int(self.sal * self.raise_amt)


e1 = employee("rohan","thareja",50000)
print(e1.fullname())
print(e1.sal)
e1.salraise()
print(e1.sal)
        
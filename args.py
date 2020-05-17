# import requests
import sys
print ("............")
print(sys.executable)
print(sys.path)

# r= requests.get("https://google.com")
# print(r.status_code)

def func(x,*args,**kwargs):
    print(x)
    print('args:',args)
    print('kwargs:',kwargs)

def lam():
    x = [1,2,3,4]
    mult = map(lambda num : num * num,x)
    print(list(mult))
    Fil = filter(lambda p: p % 2 == 0,x)
    print(list(Fil))

if __name__ == "__main__":
    func('rohan',1,2,3,fname='rohan',lname='thareja')
    lam()
    
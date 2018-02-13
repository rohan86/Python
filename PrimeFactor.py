'''program to calculate prime factors of a number '''


def prime_fact(num):
    i=2
    fact=[]
    while num != 1:

        if (div(num,i) == 0):
            fact.append(i)
            num = num/i
        else:
            i = i+1
    return fact


def div(x,i):
    if(x%i == 0):
        return 0
    else:
        return(1)



print('Enter the number whose prime factors are to be calculated')

num = eval(input())

if (type(num) == int):
    l=prime_fact(num)
    for i in l:
        print('The prime factors are :{}'.format(int(i)))
else:
    print('Enter a Numeric Value')




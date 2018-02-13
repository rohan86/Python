'''program to calculate prime factors of a number '''

import sys
import traceback
import logging


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


def main():
    try:
        num = int(input("Enter the number whose prime factors are to be calculated"))
        l=prime_fact(num)
        print('The prime factors are :{}'.format(l))
    except Exception as e:
        logging.exception('Error occurred ' + str(e))


if __name__ == "__main__":
    main()





import math


def prime_checker(number):
    sta = 1
    for i in range(2,int(math.sqrt(number))+1): # range[2,sqrt(num)]
        if(number%i==0):
            sta=0
            print("Not Prime")
            break
        else:
            continue
        
    if(sta==1):
        print("Prime")
        return sta


n = int(input())
prime_checker(number=n)
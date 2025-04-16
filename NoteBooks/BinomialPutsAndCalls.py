import math
import numpy as np
S0= 20#stock price at zero'
K= 22 #'exercise price'
sigma=  0.20 #'volatility'
dt=1.0
r=0.12  #'interest rate'
u=math.exp(sigma*math.sqrt(dt))
d=1/u
divyield=0
p=(math.exp((r-divyield)*dt)-d)/(u-d)
n=5
EurCallPrice=np.zeros([n+1,n+1])
USCallPrice=np.zeros([n+1,n+1])
EurPutPrice=np.zeros([n+1,n+1])
USPutPrice=np.zeros([n+1,n+1])

print('u',u)
print('d',d)
print('p',p)

for t in range(n,-1,-1):
    print ('t', t)
    for i in range(0,t+1,1):
        print ('i', i)
        S=S0*(u**i)*(d**(t-i))
        CallEx=max(S-K,0)  #'exercise value of the call
        PutEx=max(K-S,0)  #'exercise value of the put
        print('S', S)
        print('CallEx', CallEx)
        print('PutEx', PutEx)
        if t==n:
            EurCallPrice[t][i]= CallEx
            USCallPrice[t][i]= CallEx
            EurPutPrice[t][i]=PutEx
            USPutPrice[t][i]= PutEx

        else:
            EurCallPrice[t][i]= np.exp(-r) * ( (EurCallPrice[t+1][i+1] *p) + EurCallPrice[t+1][i]* (1-p) )
            USCallcont= np.exp(-r) * (USCallPrice[t+1][i+1]*p+USCallPrice[t+1][i]*(1-p))
            USCallPrice[t][i]=max(USCallcont, CallEx)
            EurPutPrice[t][i]= np.exp(-r) * (EurPutPrice[t+1][i+1]*p+EurPutPrice[t+1][i]*(1-p))
            USPutcont = np.exp(-r) * (USPutPrice[t+1][i+1] * (p) + USPutPrice[t+1][i] *(1-p))
            USPutPrice[t][i] = max(USPutcont, PutEx)  # Assigning the maximum value)
    print('EurCallPrice', EurCallPrice[t])
    print('USCallPrice', USCallPrice[t])
    print('EurPutPrice', EurPutPrice[t])
    print('USPutPrice', USPutPrice[t])
print(EurCallPrice[0][0])
print(USCallPrice[0][0])
print(EurPutPrice[0][0])
print(USPutPrice[0][0])

def max(x,y):
    if x>y:
        return x
    else:
        return y

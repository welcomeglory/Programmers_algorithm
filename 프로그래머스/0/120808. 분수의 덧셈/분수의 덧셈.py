import math

def solution(numer1, denom1, numer2, denom2):
    x = numer1*denom2+denom1*numer2
    y = denom1*denom2 
    gcd = math.gcd(x, y) #최대공약수
    return [x//gcd,y//gcd]
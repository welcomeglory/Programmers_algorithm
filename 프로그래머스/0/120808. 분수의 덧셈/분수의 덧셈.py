def gcd(num1, num2):
    if num1<num2:
        num1, num2 = num2, num1
    while num1%num2 != 0:
        remainder = num1%num2
        num1 = num2
        num2 = remainder
    return num2

def solution(numer1, denom1, numer2, denom2):
    denom_gcd = gcd(denom1, denom2)
    sum_denom = denom_gcd * (denom1//denom_gcd) * (denom2//denom_gcd)
    sum_numer = numer1*(sum_denom//denom1) + numer2*(sum_denom//denom2)
    
    sum_gcd = gcd(sum_numer, sum_denom)
    sum_numer //= sum_gcd
    sum_denom //= sum_gcd
    answer = [sum_numer, sum_denom]
    return answer
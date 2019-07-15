def computepay(h,r):
    if h > 40 :
        pay= 40 * r + r * 1.5 * (h - 40 )
    else :
        pay=r*h
    #return 42.37
    return pay

hrs = input("Enter Hours:")
rate= input("Enter Rate:")

#p = computepay(10,20)
#print("Pay",p)
p=computepay(float(hrs),float(rate))
print(p)

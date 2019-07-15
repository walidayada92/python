hrs = input("Enter Hours:")
rate = input("Enter rate:")
r= 10.05
try:
    h = float(hrs)
    r= float(rate)
except:
    print ("Please enter a valid number")
if h <= 40 :
    pay= rate * h
else :
    pay= r  * 40 + r*1.5*(h-40)
print(pay)

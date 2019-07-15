score = input("Enter Score: ")
try:
    scoree = float(score)
except:
    print("Enter a vaild number")
if scoree < 0.0 or scoree > 1.0 :
    print("out of range")
else :
    if scoree >= 0.9 :
        print("A")
    elif scoree >= 0.8 :
       print("B")
    elif scoree >= 0.7 :
       print("C")
    elif scoree >= 0.6 :
        print("D")
    elif  scoree < 0.6:
        print("F")
    else :
        print("error")

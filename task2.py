largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum=int(num)
    except:
        print("Invalid input")
    if smallest is None:
        smallest=fnum
    #    continue
    elif largest is None  :
        largest = fnum
    #    continue
    elif fnum>largest:
        largest=fnum
    #    continue
    elif fnum<smallest:
        smallest=fnum
    #    continue
#    largest=num
#    if num > largest:
#        largest=num
#    else:
#        smallest=num
print("Maximum is",largest )
print("Minimum is", smallest)

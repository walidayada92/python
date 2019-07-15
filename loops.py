#for i in [5, 4 , 3 , 2 ,1] :
#    print (i)
#n=5

#while n > 0 :
#    print(n)
#    n = n - 1

while True:
    line=raw_input('>')
    if line[0]=="#":
        continue
    if line=='done':
        break
    print(line)

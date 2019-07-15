import re
fh = open('regex_sum_150684.txt')
sum = 0
for line in fh:
    y= line.rstrip()
    if re.search('[0-9]+', y) :
        yy  = re.findall('[0-9]+',y)
        for i in yy:
           sum += int(i)
print (sum)

#    lst.append(yy)
    #float_num= float(yy)
    #sum  = sum + yy

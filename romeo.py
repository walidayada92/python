fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  # x= line.rstrip()
   y= line.rstrip()
   words=y.split()
   for word in words :
       lst.append(word)
   #lst.sort()
   o=list(set(lst))
   o.sort()
print(o)

text = "X-DSPAM-Confidence:    0.8475";
ps=text.find('0')
num=text[ps:]
print(float(num))
print("fknmn".upper)



# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
mh=fh.read()
sh=mh.rstrip()
print(mh.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count+1
        #colon = line.find('X-DSPAM-Confidence:')
        #app = line.find('0')
        ans = line[19:].lstrip()
        x = float(ans)
        #print('testing', x)
        num = num+x
        #print('count',count,'num',num)
        avg = num/count
print('Average spam confidence: ', avg)
print("Done")
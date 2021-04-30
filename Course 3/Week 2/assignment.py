import re

fh=open('regex_sum_973096.txt')

nums=list()
for line in fh:
    num=re.findall('[0-9]+',line)
    if len(num)==0: continue
    for val in num:
        nums.append(val)

sum=0
for val in nums:
    sum=sum+int(val)

print(sum)

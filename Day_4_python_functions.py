#Using fucntion in python

# using map function :
# use data tranformation

list1=[1,2,3,4,5]
squares=map(lambda x:x**2,list1)
print(list(squares))

# using reduce function
#  for aggregating datas

# getting sum of the list without using sum fucntion

from functools import reduce
total_sum=reduce(lambda x,y:x+y,list1)
print(total_sum)

# using enumerate function
# used for the loop sequence along with the index

for index,value in enumerate(list1,start=1):
    print(f"{index}:{value}")

# using zip function
# combining values

list2=["Santosh","mani","Kani","thani","vani"]
list3=list(zip(list1,list2))
print(list3)

# filter function
# using filter values

list4=filter(lambda x:x<3,list1)
print(list(list4))

# using any return true id any one is true

any_value=any(x%2==0 for x in list1)
print(any_value)

# any funtion that returns false if any one is false

all_value=all(x%2==0 for x in list1)
print(all_value)

# using sorted

sorted_list=sorted(list1,reverse=True)
print(sorted_list)

dict={3:"sandy",1:"candy",2:"mandy"}
for key in sorted(dict):
    print(f"{key}:{dict[key]}")

# using values

items_Sorted=sorted(dict.items(),key=lambda item:item[1])
print(items_Sorted)

# using regex

import re
test="My name is santosh"
match=re.match(r"My name is (\w+)",test)
print(match.group(0),match.group(1))

pattern = r"(?:Mr|Mrs|Ms)\.?\s\w+"
text = "Ms. Taylor"
match = re.search(pattern, text)
print(match.group()) 

text = "Email me at test@example.com"
match = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(match.group()) 

phone = "9876543210"
if re.fullmatch(r'[6-9]\d{9}', phone):
    print("Valid")
else:
    print("invalid")

text = "My postal index is 636122 and code is 636133"
print(re.findall(r'\d+', text))  

print(re.sub(r'\d+',"####",text))

# generator concepts

def fun1(x):     
    count=0
    while(x>=0):
        yield count
        count=count+1
        x=x-1
for i in fun1(10):
    print(i)
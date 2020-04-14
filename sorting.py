# Sorting string elements using built-in and without builtin functions

# Method 1

a="developer"
x="".join(sorted(a))
print(x)

# Method 2

test=input("ENTER THE STRING:")
s=""
l=list(test)
print(l)
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
for m in l:
    s=s+m
print(s)

# to sort the words

data="sorting python examples"
x=data.split()
x.sort()
for i in x:
    print(i)

# Sorting list elements using built-in and without builtin functions

# Method 1

lst=['mango','cherry','kiwi','strawberry']
lst.sort()
print(lst)

# Method 2 (ascending-descending)

data=[23,45,96,34,75]
# data=['k','i','t','e']
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if(data[i]>data[j]):
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
print(data)

# Method 3 (descending-ascending)

data=[23,45,96,34,75]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if(data[i]<data[j]):
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
print(data)

# (OR)

data=['beauty','of','the','rose']
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if(data[i]<data[j]):
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
print(data)


# Sorting tuple elements using built-in

tup=[53,85,16,94,75]
print(sorted(tup))

# Sorting dictionary elements using built-in and without builtin functions

# Method 1

data={'name':'xyz','sub':'maths','id':12,'marks':87}
for k in sorted(data.items()):
    print(k,end=" ")

# (OR)

data={'name':'xyz','sub':'maths','id':12,'marks':87}
for i in sorted(data):
    print((i, data[i]), end=" ")

# Method 2

from _collections import OrderedDict
test = {'ravi':'10','rajitha':'9','vinutha':'15','yashu':'2'}
test1= OrderedDict(sorted(test.items()))
print(test1)
print(type(test1))

# Method 3 (Sorting dict by keys)
data={'name':'xyz','sub':'maths','id':12,'marks':87}
s=[]
for i in sorted(data.keys()):
    s.append(i)
print(s)

# Method 4 (Sorting dict by values)
data={'a':15,'b':29,'c':3}
s=[]
for i in sorted(data.values()):
    s.append(i)
print(s)


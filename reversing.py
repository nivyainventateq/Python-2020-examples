# Reversing a String with Builtin function and without Function

# Method 1
a='Helloworld'
print(a[::-1])

# Method 2
b='software'
s=""
for i in b:
    s=i+s
print(s)

# Method 3
c='Developer'
l=''.join(reversed(c))
print(l)

# Method 4
d='Organization'
s=""
l=len(d)-1
while(l>=0):
    s=s+d[l]
    l=l-1
print(s)

#  List Reverse with Builtin function and without Function

# Method 1
data=[10,97,'lion',43,'tiger']
print(data[::-1])

# Method 2
data=[10,97,87,43]
data.reverse()
print(data)

# Method 3
data=[76, 23, 45, 14,87]
s=[]
for i in data:
    s.insert(0,i)
print(s)


# Method 4
lst=[16, 23, 50, 44, 94]
l=[]
for i in reversed(lst):
    l.append(i)
print(l)

# Method 5
data=[1,2,3,4]
s= []
l = len(data)-1
while l>= 0:
    s.append(data[l])
    l=l-1
print(s)

# Method 6

lst=[2,456,85,14]
i = 0            # first item
j = len(lst)-1   # last item
while i<j:
    lst[i],lst[j] = lst[j],lst[i]
    i += 1
    j -= 1
print(lst)

#  Tuple Reverse with Builtin function and without Function

# Method 1
test=(1,2,3,4,5)
print(test[::-1])

# Method 2
test=('a','l','k','j')
x=reversed(test)
print(tuple(x))

# Method 3
tup=(16, 23, 50, 44, 94)
for i in range(len(tup)):
    print(tup[-(i+1)])

#  Dictionary Reverse with Builtin function and without Function

#Method 1
data={'name':'xyz','age':12}
mydict={}
for k,v in data.items():
    d={k:v}
    d.update(mydict)
    mydict=d
print(mydict)

# Method 2 (reversing key - value and value -key)

data={'name':'xyz','age':12}
print(data)
s={v:k for k,v in data.items()}
print(s)

# method 3 (reversing keys)

t={'a':1,'b':2,'c':3}
for i in reversed(sorted(t.keys())):
    print(i)
    # print(t[i])




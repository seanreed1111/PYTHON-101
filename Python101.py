#!/usr/bin/env python
# coding: utf-8

# In[88]:


# Note: ALWAYS USE PYTHON3. 
# MAKE SURE YOU GET PYTHON3 answers when you search google!


# In[ ]:





# In[89]:


h = 20
print(h)


# In[90]:


id(h)


# In[91]:


x = 20


# In[92]:


id(x)


# In[ ]:





# In[93]:


h = 'little'
print(h)


# In[94]:


g = "big"
print(g)


# In[95]:


print(type(g))


# In[96]:


h = 20
print(type(h))


# In[97]:


f = 65.7
type(f)


# In[98]:


20+45


# In[99]:


20.5 + 45


# In[100]:


20+ "20"  # ERROR


# In[ ]:


20 + int("20") #OK


# In[ ]:


20 + int("hello") #ERROR


# In[ ]:





# In[ ]:


t = int(9.5)
print(t)
print(type(t))


# In[ ]:


item = str(9)
item


# In[ ]:


type(item)


# In[ ]:


dir(item)


# In[ ]:


dir(str)


# In[ ]:


type(9)


# In[ ]:


dir(9)  

# 9 is an int OBJECT, with attributes and methods. We will ignore the dunder methods 
#(dunder => double underscore)


# In[101]:


dir(int)


# In[102]:


#float, str, int, bool 
# these are the 'basic' types 


# In[103]:


5 > 4  #This is a boolean expression. Evaluates to True or False.


# In[104]:


greater = 5 > 4
print(greater)  # greater is of type bool


# In[105]:


type(greater)


# In[ ]:





# In[106]:


#Container Types: list, tuple, dict


# In[107]:


my_list = [] #empty list. Like arrays in other languages


# In[108]:


type(my_list)


# In[109]:


# IMPORTANT: Avoid using the word 'list' AS A VARIABLE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# In[110]:


print(my_list)


# In[111]:


# use lists to hold other types. Lists can even contain other lists!


# In[112]:


my_list = [1,2,3,4,5]
print(my_list)


# In[113]:


my_list = [45.7, 99.9]
my_list


# In[114]:


my_list = [5, 55.5]
print(my_list)


# In[115]:


my_list = ['strings', 5] #DONT DO THIS. Use lists to hold objects of the same type.


# In[116]:


#Aside: Use tuples to hold related objects of different types  
my_tuple = ('alex', 22, "1313 Mockingbird Lane")


# In[117]:


my_list = [5, 55.5]
print(my_list)


# In[ ]:





# In[118]:


# The first item in a list is at index 0
my_list[0]


# In[119]:


# The second item in a list is at index 1
my_list[1] 


# In[120]:


my_list[2] #ERROR. There is nothing at index 2


# In[ ]:


len(my_list) # my_list has two elements. length = 2


# In[ ]:


# tuples

t1 = 'Alex', 'Trebec', '79'
t2 = 6,7,8,9,10
print(t1)
print(t2)


# In[ ]:


type(t1)


# In[ ]:


t3 = 6,7
t3


# In[ ]:


t3[0] , t3[1]


# In[ ]:


t3 = 100, 200 # this works. It is ok to move the post-it note, t3, somewhere else.
t3


# In[ ]:


t3[0] = 2700 # this does not work. You cannot change the elements of a tuple after creation.


# In[ ]:


my_list = ['hello', 'sean']
my_list


# In[ ]:


my_list[0] = 'sun' #this works. Totally ok to change the elements of a list at any time.
my_list


# In[ ]:


type(my_list)


# In[ ]:


dir(list)


# In[ ]:


# List Methods


# In[ ]:


my_list.append(10)
print(my_list)


# In[ ]:


my_list.append([1,20,30,40])
my_list


# In[ ]:


my_list = ['hello', 'sean']


# In[ ]:


my_list.extend(["one", "two", "three"])
my_list


# In[ ]:





# In[ ]:


my_list = [1,2,3]
my_list


# In[ ]:


my_list.extend([8,9,11])
print(my_list)


# In[ ]:


my_list.append([100,200,300])
my_list


# In[ ]:


my_list = [1, 5, 10]


# In[ ]:


#danger
my_list.reverse() #reverse destroys and replaces the original list
print(my_list)


# In[ ]:


my_list


# In[ ]:


#danger
my_list = [333, 5, 10]
my_list.sort()
print(my_list) #sort destroys and replaces the original list


# In[ ]:


result = my_list.sort()


# In[ ]:


print(result)


# In[ ]:


type(result)


# In[ ]:


8*result # None cannot be used in calculations. It will give you errors that are hard to understand.


# In[ ]:





# In[ ]:


n * 8


# In[ ]:


my_list = [45,6,333]


# In[ ]:


#sorted makes a new list and leaves the original list unchanged

n2 = sorted(my_list)
n2


# In[ ]:


id(my_list), id(n2) #ids are different, so they are different objects


# In[ ]:


my_list


# In[ ]:


sorted(my_list) #reverse defaults to False, so you don't need to pass it


# In[ ]:


sorted(my_list, reverse=False) #same answer


# In[ ]:


sorted(my_list, reverse=True) #if you pass reverse=True, sorts from biggest to smallest


# In[ ]:


sorted #sorted is a global function


# In[ ]:





# In[ ]:


my_list = [333, 5, 10]


# In[ ]:


new_list = reversed(my_list)


# In[ ]:


print(my_list) #original list unchanged


# In[ ]:


new_list #python is LAZY. Does not want to reverse the list. 
# Python Made an object that tells it how to reverse the list instead.


# In[ ]:


print(new_list)


# In[ ]:


#reversed is a LAZY operator
print(new_list) #this makes an object, but list has not been reversed yet!


# In[ ]:


my_list


# In[ ]:


list(new_list)


# In[ ]:


new_list[0]


# In[ ]:


print(list(new_list)) #can see the result if you explicitly convert to a list


# In[ ]:


my_list


# In[ ]:





# In[ ]:


r = range(10) # range is also LAZY.
r


# In[ ]:


print(r)


# In[ ]:


list(r) # converting to a list forces Python to evaluate the range.


# In[ ]:





# In[ ]:


print(range(1,1000000000000000000000)) # range is a lazy data type. 


# In[ ]:





# In[ ]:


#python is a whitespace significant language
#indentation matters!
for i in range(10):
    print(i) # inside of the loop
print(100) #outside of the loop


# In[ ]:


for i in range(10):
print(i)  #whitespace is 100% necessary!


# In[ ]:


for i in range(10):
    print(i)


# In[ ]:


for i in range(9): #starts at zero if no default first value is given
    print(i)


# In[ ]:


for i in range(1,12):
    print(i)


# In[ ]:


for i in range(1,11,2):
    print(i)
print('done')


# In[ ]:


for i in range(1,16,2): #start at 1, go up to but not including 11, count by 2s
    print(i)


# In[ ]:


for i in reversed(range(10)):
    print(i)


# In[ ]:


for i in range(10,0,-1):
    print(i)


# In[ ]:


my_list = ['a', 'b', 'c', 'd']
for letter in my_list:
    print(letter)


# In[ ]:


for number in range(0,3):
    print(number)


# In[ ]:





# In[ ]:


for item in reversed(my_list): #reversed does not change the original list
    print(item)


# In[ ]:


[3,4] + [5,6]


# In[ ]:


my_list


# In[ ]:


for index, item in enumerate(my_list): #makes my_list into a tuple
    print(index, item)


# In[ ]:


for thing in enumerate('abcd'): #makes my_list into a tuple
    print(thing)


# In[121]:


my_str  = 'abcd'
my_str[0]


# In[122]:


l = ['abcd', 'efgh']


# In[123]:


for thing in enumerate(l): #makes my_list into a tuple
    print(thing)


# In[ ]:





# In[124]:


mt = 5,6 #mt is of type tuple even though it doesn't have parentheses!
ml = [10,11] #list
ml.extend(mt)
print(ml)


# In[ ]:





# In[125]:


# dictionaries


# In[126]:


d = {"a":1, "b":2, "c":3}
d


# In[127]:


d['a']


# In[128]:


# this is a comment
for key in d:
    print(key, d[key])


# In[ ]:





# In[129]:


dir(dict)


# In[130]:


md = {'first':1, 'second':2, 'fourth':4}
print(md)


# In[131]:


md = {'first':"The Matrix", 'second':"Superman", 'fourth':'Batman'}
print(md)


# In[132]:


md['first'] = "Batman Begins"
print(md)


# In[133]:


md['second'] = None


# In[ ]:





# In[134]:


md.items()


# In[135]:


md.keys()


# In[136]:


md.values()


# In[137]:


for k in md: #goes through the keys one at a time
    print(k,md[k])


# In[138]:


#changes the value associated with the key 'third'
md['third'] = "Ralph Breaks the Internet"
for k in md:
    print(k,md[k])


# In[139]:


#changes the value associated with the key 'first'
md['first'] = ("Batman Begins", 3) 
print(md)


# In[140]:


md['second']


# In[ ]:





# In[ ]:





# In[ ]:





# In[141]:


#if elif else
x = -5

if x > 5:
    print("greater than 5")
    
elif x == 5:
    print("Equal to 5")
else:
    print("less than 5")


# In[142]:


x = 55

if x > 5:
    print("greater than 5")


# In[143]:


x = -5

if x > 5:
    print("greater than 5")
    
else:
    print("less than 5")


# In[144]:


x = 5

if x > 5:
    print("greater than 5")
elif x == 5:
print("Equal to 5")


# In[ ]:





# In[ ]:





# In[145]:


def myfunc():
    print("ran the function")


# In[146]:


g = myfunc()
type(g)


# In[147]:


def myfunc():
    print("ran the function")
    return "done"


# In[148]:


g = myfunc()
type(g)


# In[ ]:





# In[ ]:





# In[149]:


myfunc()


# In[150]:


def f():
    print("ran the function")


# In[151]:


myvar = f()
myvar


# In[152]:


type(myvar)


# In[ ]:





# In[153]:


def myfunc2(): #correct way to write function that doesn't do anything
    pass


# In[154]:


def myfunc3(): #not valid


# In[ ]:





# In[155]:


def myfunc4(val):
    return val+val


# In[156]:


myfunc4("hello")


# In[ ]:





# In[ ]:





# In[157]:


def myfunc5(val):
    assert type(val) == int
    return val+val
myfunc5('hello')


# In[ ]:





# In[ ]:





# In[158]:


def myfunc4(val="hello there"):
    print(val)

myfunc4()


# In[159]:


myfunc4("hello")


# In[160]:


# function can return a value
def myfunc5(val="hello there"):
    return val

var = myfunc5()
var2 = myfunc5("spike")
print(var, var2)


# In[161]:


#functions can return any number of different values as a tuple
def myfunc6(val="hello there"):
    length = len(val) 
    return length, val    # length, val is a tuple

result = myfunc6("Birdbox")
print(result)


# references: 
# 
# https://github.com/jakevdp/WhirlwindTourOfPython
# https://snakify.org/en/

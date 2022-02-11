# =============================================================================
# most basic
# =============================================================================

# to create a dictionary :
price=dict()
# or
price={}
# just like how we create lists

# add elements
price['apple']=2
price['banana']=3

# =============================================================================
# .get()
# =============================================================================

# to get an element which exists in the dictionary (or not):
x=price.get('bana',0) # if 'bana' doesn't exist in the dictionary, then x equals to 0

# an application of .get()
#counting number in a list, put the results in a dictionary
res=dict()
liste=['txt','pdf','ai','pdf','docx','m','txt','xlsm','R','R','py']
for formats in liste:
    res[formats]=res.get(formats,0)+1


# =============================================================================
# inspect a dictionary
# =============================================================================
# print the keys of a dictionary
print('print the keys of a dictionary')
print(list(res))
print(res.keys())
# print the values of a dictionary
print('print the values of a dictionary')
print(res.values())
# print both keys and values
print('print both keys and values')
print(res)
print(res.items())
    
    
# =============================================================================
# two iterations (a Python only feature)
# =============================================================================
prices={'Banana':4,'Pineapple':3,'Orange':1.5}
for fruit,price in prices.items():
    print(fruit,' ',price)


# =============================================================================
# An exercise for fun, find which word appears the most frequently in a text
# =============================================================================
# The basic logic is, firstly read the text file, split it into words, then put the words into a dictionary,
# then find the max in the dictionary
hist=dict()
fhand=open('romeo.txt')
# put it in a dictionary
for line in fhand:
    words=line.split()
    for word in words:
        hist[word]=hist.get(word,0)+1
# inspect the dictionary
for keys,values in hist.items():
    print(keys,'\t\t',values)

print('\n')
print('-------------------')
print('\n')
# find the word which appears the most frequently
maxWord=None
maxCount=0
for word,count in hist.items():
    if maxCount<count:
        maxWord=word
        maxCount=count
# in case there are several max
for word,count in hist.items():
    if count==maxCount:
        print(word,'\t',count)


# =============================================================================
# Exercise 2: 
# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
# =============================================================================
# count which day of the week the email is send
fhand=open('mbox-short.txt')
day=None
res=dict()
for line in fhand:
    if line.startswith('From '):
        day=line.split('@')[1].split()[1] # or just .split()[2]
        res[day]=res.get(day,0)+1
print(res)



# =============================================================================
# Exercise 3:
# count how many messages come from each mail address, and find who sends the most of the emails
# =============================================================================
# count messages -----------------------------
fhand=open('mbox-short.txt')
res={}
for line in fhand:
    if line.startswith('From '):
      address=line.split()[1]
      # put the address into the dictionary
      res[address]=res.get(address,0)+1
# print the result
for key,value in res.items():
    print(key,'\t', value)
# find the max ---------------------------
maxKey=None
maxValue=0
# two methods to find the max, method 1:
for key in res:
    if res[key]>maxValue:
        maxValue=res[key]
        maxKey=key
# method 2
for key,value in res.items():
    if value>maxValue:
        maxValue=value
        maxKey=key
print('\n')
print('The maximum is :')
print(maxKey,maxValue)










    
    
    








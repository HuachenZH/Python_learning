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






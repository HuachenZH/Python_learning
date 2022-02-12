# =============================================================================
# intro
# =============================================================================

# tuple is like list, but it cannot be modified.
# Tuple is more efficient, better memory-used than list, so programmers use tuple for temporary variables

# To create a tuple:
a=(10,5)
a=10,5 # we can even omit the ()

# An interesting remark of tuple, when comparing tuples:
(0,1,20000)<(0,2,3)
# it returns True. Python firstly compare 0 and 0, when the item is equal, Python goes to the second : 1 and 2. 1 is smaller then 2, so True.
# Once Python gets the answer, it stops comparing the next.



# =============================================================================
# Sort a dictionary by key and by value
# =============================================================================
d={'a':10,'c':5,'b':7}
# sort it by the key
print('sort by key')
for i in sorted(d.items()):
    print(i)
print('\n')
# sort it by values by creating a new list where value become key
print('sort by value')
liste=list()
for key,value in d.items():
    liste.append((value,key))
print(sorted(liste))
for i in sorted(liste):
    print(i)



# =============================================================================
# get the top 10 most commun words in a text
# =============================================================================
bag=dict()
fhand=open('computer.txt')
# put the words and their counts into a dictionary
for line in fhand:
    for word in line.split():
        bag[word]=bag.get(word,0)+1
        
# make a list, with tuples as elements, first count, then word
# (so that count becomes key, word becomes value)
liste=list()
for word,count in bag.items():
    liste.append((count,word))
liste=sorted(liste,reverse=True) # sort the list
for i in range(10): # print the top 10
    print(liste[i])
print('\n')
for i in liste[:10]: # another way to print the top 10
    print(i)
print('\n')

for value,key in liste[:10]: # a third way to print the top 10
    print(key,'\t',value)  
# remark about the double iteration :----------------!!!!!!!!!!!!!
# before with dictionary, double iteration can be executed when: for key,value in dictionary.items()
# and dictionary.items() returns a list of tuples, which is the same with the code above (liste is also a list of tuples)

# even a triple iteration can work :
tmplist=[(1,2,3),(3,5,1)]
for a,b,c in tmplist:
    print(a,b,c)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# incredible syntax, for in parenthese of a function
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
c={'a':10,'b':1,'e':22}
print(sorted([(v,k) for k,v in c.items()]))                     # output: [(1, 'b'), (10, 'a'), (22, 'e')]
print(sorted([(v,k) for k,v in c.items()],reverse=True))        # output: [(22, 'e'), (10, 'a'), (1, 'b')]
print([(i) for i in c])                                         # output: ['a', 'b', 'e']
print([(v,k) for k,v in c.items()])                             # output: [(10, 'a'), (1, 'b'), (22, 'e')]

# attention, the [ ] is important, if not, there won't be traceback but the output is not correct
# [ ] means, hi python, this is a list
# and the variables before "for" must be envelopped by ()




# =============================================================================
# Exercise 1
# With mbox-short.txt, find the person who send the most of the emails
# =============================================================================
fhand=open('mbox-short.txt')
bag=dict()
tmp=None
# create the dictionary
for line in fhand:
    if line.startswith('From '):
        tmp=line.split()[1]
        bag[tmp]=bag.get(tmp,0)+1        
candy=list() # to make a list, we can sort a list but not a dictionary

# the correct answer is, cwen@iupui.edu has sent emails the most, which is 5 times
# however i found three ways to get the answer. 

# method 1, the most classic way
for k,v in bag.items():
    candy.append((v,k))
candy=sorted(candy,reverse=True)
print(candy[0])
# output : (5, 'cwen@iupui.edu')
# candy is a list of size of 11

# method 2, create a list with all the senders sorted, then print the first element
candy.append(sorted([(v,k)for k,v in bag.items()],reverse=True))
print(candy[0][0])
# the output is : (5, 'cwen@iupui.edu')
# candy is a list of size of 1 ! it means that in candy, there is only one element, and this element is another list of 11 element
# in other word, we need the first element of the first element, so that's why there's [0][0]
# list in a list. There is one way to unlist it:
candy=candy[0]

# method 3: create a list with only one element, which is the most sender
candy.append(sorted([(v,k)for k,v in bag.items()],reverse=True)[0])
print(candy)
# output : [(5, 'cwen@iupui.edu')] camparing to other two methods, there is [] in this output which others don't have



# =============================================================================
# Exercise 2
# find the distribution of hours of each mail
# =============================================================================
fhand=open('mbox-short.txt')
hour=None
bag=dict()
# create the dictionary
for line in fhand:
    if line.startswith('From '):
        hour=line.split()[5].split(':')[0]
        bag[hour]=bag.get(hour,0)+1
# make it a list
sugar=list()
sugar.append(sorted([(k,v)for k,v in bag.items()])) # sugar is a list of one element, which is another list of 12 tuples
sugar=sugar[0] # to unlist one time, so sugar becomes a list of 12 tuples
# print in a python-one-liner way:
print([(k) for k in sugar])  # the output is : [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]
# print in a normal way:
for k in sugar:
    print(k)
# the output is:
# ('04', 3)
# ('06', 1)
# ('07', 1)
# ('09', 2)
# ('10', 3)
# ('11', 6)
# ('14', 1)
# ('15', 2)
# ('16', 4)
# ('17', 2)
# ('18', 1)
# ('19', 1)



# =============================================================================
# Exercise 3
# Read a text file in all lower case, count how many times each letter a-z appears. Do not count .!() etc
# =============================================================================
fhand=open('intro.txt')
bag=dict()
# creat a dictionary with all the letters inside
for line in fhand:
    line=line.lower()
    line=line.split()
    for word in line:
        for i in range(len(word)):
            bag[word[i]]=bag.get(word[i],0)+1
# then i found there is still special characters like ! ( ) ' inside, so i need to find a way to clear them
            
# for k in bag:
#     if k<'z':
#         del bag[k]  # in this way, traceback will say that the dictionary changes size during the iteration. Unlike Matlab, this is not acceptable in Python 
bag2=dict() # so i need to create a new dictionary
for k in bag:
    if k<='z' and k>='a':
        bag2[k]=bag[k]

# print the result, in alphabetic order. So need to make a list to sort it
sugar=list()
sugar.append(sorted([(k,v)for k,v in bag2.items()]))
sugar=sugar[0]
for k,v in sugar:
    print(k,'\t',v)




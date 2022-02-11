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













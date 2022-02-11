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
























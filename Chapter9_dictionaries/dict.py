# to create a dictionary :
price=dict()
# or
price={}
# just like how we create lists

# add elements
price['apple']=2
price['banana']=3

# to get an element which exists in the dictionary (or not):
x=price.get('bana',0) # if 'bana' doesn't exist in the dictionary, then x equals to 0

# an application of .get()
#counting number in a list, put the results in a dictionary
res=dict()
liste=['txt','pdf','ai','pdf','docx','m','txt','xlsm','R','R','py']
for formats in liste:
    res[formats]=res.get(formats,0)+1




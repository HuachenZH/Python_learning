#read a text file and in all lower case, count the number of all letters a to z
fhand=open('intro.txt')
bag=dict()
for line in fhand:
    line=line.lower()
    line=line.split()
    for word in line:
        for i in range(len(word)):
            bag[word[i]]=bag.get(word[i],0)+1
# for k in bag:
#     if k<'z':
#         del bag[k]
bag2=dict()
for k in bag:
    if k<='z' and k>='a':
        bag2[k]=bag[k]

# print the result, in alphabetic order. So need to make a list to sort it
sugar=list()
sugar.append(sorted([(k,v)for k,v in bag2.items()]))
sugar=sugar[0]
for k,v in sugar:
    print(k,'\t',v)

# compute the percentage
total=0
listValue=list()
for i in sugar:
    listValue.append(i[1])

listPercentage=listValue
tmp=sum(listValue)
# for i in range(len(listPercentage)):
#     listPercentage[i]=listPercentage[i]/tmp

# out=[a+b for a,b in zip(listValue,listPercentage)]

# Normally, in the variable explorer, listValue is a list a value 1766,258,561...
# and listPercentage is a list of percentage
# the problem is with the line 33 and 34, if i don't put them on comments, listValue will become the same as listPercentage
# don't know why

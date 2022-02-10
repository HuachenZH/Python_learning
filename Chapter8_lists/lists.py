
# ask user to input numbers, then output the average value
num=[]
while True:
    inp=input('Give a number: ')
    if inp=='done':
        break
    try:
        value=float(inp)
    except:
        print('Not a number')
        continue
    num.append(value)
    
average=sum(num)/len(num)
print('The average is ',average)



"""
Exercices 4
To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.
"""
out=[]
fhand=open('romeo.txt')
for line in fhand:
    piece=line.split()
    for word in piece:
        if word not in out:
            out.append(word)
out.sort()
print(out)




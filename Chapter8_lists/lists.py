
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



"""
Exercise 5
MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
"""
out=[]
fhand=open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        out.append(line.split()[1])
print(out)
print('\n')
print('You have in total ',len(out),'emails in mbox')









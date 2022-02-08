# To open files in Python :
# fhand=open()
# remark : the function open() creates a handle

# open file
fhand=open('data.txt')

# Two methods to print the file in the console :
# method 1, use for and read the handle line by line
fhand=open('data.txt')
for line in fhand:
    print(line)
	
# method 2, use .read() to read the whole file :
fhand=open('data.txt')
inp=fhand.read() # remark : inp is a str
print(inp)


# A simple code to open and read file :
fname=input('Type file name :  ')
try:
    fhand=open(fname)
except:
    print('The file does not exist.')
    quit()

for line in fhand:
    print(line)


"""
Exercise : 
Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence:0.8475
When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
"""
fhand=open('mbox-short.txt')
total=0
count=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        index=line.find(':')
        total=total+float(line[index+1:])
        count=count+1
average=total/count
print('Average spam confidence : ',average)

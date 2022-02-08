
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



start="11:06 PM"
duration="2:02"

# time=start.split(' ')[0].split(':')
# time=[int(i) for i in time if i.isdigit()]
time=[int(i) for i in start.split(' ')[0].split(':') if i.isdigit()]
periodFlag=start.split(' ')[1]

hour_orin=time[0] # the original hour
min_orin=time[1] # the original minute

hour_2add=int(duration.split(':')[0])
min_2add=int(duration.split(':')[1])

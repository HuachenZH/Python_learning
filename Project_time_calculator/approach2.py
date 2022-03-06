# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:51:54 2022

@author: e^(j·2pi)
"""
# this is just a temporary script
# try approach 2
from math import floor

start="6:30 PM"
duration="205:12"
# expected: 1:08 AM (next day)

# time=start.split(' ')[0].split(':')
# time=[int(i) for i in time if i.isdigit()]
time=[int(i) for i in start.split(' ')[0].split(':') if i.isdigit()]
periodFlag=start.split(' ')[1]

hour_orin=time[0] # the original hour
min_orin=time[1] # the original minute

hour_2add=int(duration.split(':')[0])
min_2add=int(duration.split(':')[1])




# a minute is a level. One day has 24*60 levels, a time corresponds to a specific level
# original level:
if periodFlag=='AM':
    level_orin=hour_orin*60+min_orin
elif periodFlag=='PM':
    level_orin=hour_orin*60+min_orin+12*60
else:
    level_orin=-1
    print('Invalid period (not "AM" or "PM")')
# level to add:
level_2add=hour_2add*60+min_2add
# new level in absolute scale:
level_new_abs=level_orin+level_2add
print('level_new_abs: ',level_new_abs)
# new level in relative scale:
level_new_rel=level_new_abs%1440 # new level in 1440 lv =68
print('level_new_rel: ',level_new_rel)
# new minute:
min_new_rel=level_new_rel%60
print('min_new_rel: ',min_new_rel)
# new hour:
hour_new_rel=floor(level_new_rel/60)%12
if hour_new_rel==0:
	hour_new_rel=12
print('hour_new_rel: ',hour_new_rel)

# new preiod:
if level_new_rel<=719:
    periodFlag_new='AM'
else:
    periodFlag_new='PM'
print('periodFlag_new: ',periodFlag_new)


# in minute part, '6' must change to '06'
tmp=''
if len(str(min_new_rel))<2:
    tmp='0'+str(min_new_rel)
else:
    tmp=str(min_new_rel)

# change date or not, if yes, how many days later:
xDaysLater=floor(level_new_abs/1440)
print('xDaysLater: ',xDaysLater)
out=str(hour_new_rel)+':'+tmp+' '+periodFlag_new
if xDaysLater<1:    # date isn't changed, in the same day
    # return
    print(out)
elif xDaysLater==1: # exactly one day later
    out+=' (next day)'
    # return
    print(out)
else:
    out+=' ('+str(xDaysLater)+' days later)'
    # return
    print(out)


# what i've learnt in this verison:
    # headache when there is too many variables
    # there is always a way to optimize the logic and syntax
# for next version:
    # put the code in to time_calculator.py

# ended with this script. Move on to time_calculator.py





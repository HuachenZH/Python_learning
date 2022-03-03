# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""

# stupidest approach, pur string.
# in this beta version, just to print one arithmetic format

inp="32 + 8"
listt=inp.split(' ')
res=int(listt[0])+int(listt[2])
larger=max(len(i) for i in listt)+2

out=''
if len(listt[0])>len(listt[2]):
    out+='  '+listt[0]+'\n+'
    for i in range(len(listt[0])-len(listt[2])+1):
        out+=' '
    out+=listt[2]
    out+='\n'
    for i in range(larger):
        out+='-'
    out+='\n'
    for i in range(larger-len(str(res))):
        out+=' '
    out+=str(res)
print(out)
# The output is:
#   32
# +  8
# ----
#   40


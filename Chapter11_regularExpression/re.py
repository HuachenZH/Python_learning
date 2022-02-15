import re # import the library of regular expression


# =============================================================================
# in the file mbox-short.txt, extract all the name of sender of email
# =============================================================================
import re
fhand=open('mbox-short.txt')
tmp=''
for line in fhand:
    line=line.strip()
    if re.search('^From:',line): # if the line starts with 'From:'
        tmp=re.findall('(\S+?)@',line)
        print(tmp)

# Cf. regular expression cheat sheet
# \S non white space
# + quantity, one or more
# ? means no greedy extract
# () means where to start and end the extract
# @ not a special symbol, it's what i would like to find

# so (\S+?)@ means, extract a bloc of str which starts by a no-white space, continue extracting, until the first @ met, and do not extract @


# the code can still be simplified :

import re
fhand=open('mbox-short.txt')
tmp=''
for line in fhand:
    line=line.strip()
    tmp=re.findall('From: (\S+)@',line)
    print(tmp)
# how ever tmp is a list of matched results, when there is nothing matched, tmp is [] an empty list, the output will be a horde of []
# so version 3 :
import re
fhand=open('mbox-short.txt')
tmp=''
for line in fhand:
    line=line.strip()
    tmp=re.findall('From: (\S+)@',line)
    if tmp != []:
        print(tmp)


#  http://www.dr-chuck.com/page1.htm

# =============================================================================
# By using regular expression, get the host name dr-chuck.com
# =============================================================================
import re
tmp='http://www.dr-chuck.com/page1.htm'

out=re.findall('\.(\S+)/',tmp)

import xml.etree.ElementTree as ET
# firstly import the package xml.etree.ElementTree, as the name is long, we give it a new name ET


# =============================================================================
# parse an XML from a string constant
# =============================================================================
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">+1 734 303 4456</phone>
  <email hide="yes" />
  <gender>Male</gender>
</person>'''

# parse an XML from the string data
tree=ET.fromstring(data)
tree=ET.XML(data) # the same as the previous line
# we can see in the variable explorer that the type is the variable tree is "etree.ElementTree.Element", the size is 4, because in the "person", there are "name", "phone", "email", and "gender"
# if double click tree, spyder shows all the methods and wether callable or not

print(tree.find('name').tag) # print the tag of name, so the output is : name
print(tree.find('phone').text) # print the text of the tag name, so the output is : Chuck



# =============================================================================
# multiple nodes
# not sure about the syntax of XML
# =============================================================================

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <names>
          <name x="1">Chuck</name>
          <name x="2">Norris</name>
          <name x="3">sev</name>
      </names>
    </user>
    <user x="7">
      <id>009</id>
      <names>
          <name x="1">Brent</name>
      </names>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user/names/name') # here inside the quoted is the path, unlike re.findall. This is not regular expression!
print(lst) # output is weird: [<Element 'name' at 0x000001EF41CC28B8>, <Element 'name' at 0x000001EF41CC2188>, <Element 'name' at 0x000001EF41CC2A48>, <Element 'name' at 0x000001EF41CA2908>]
print('count:', len(lst)) # in this case, len is 4

for item in lst:
	print(item.find("name"))
# still doubt about the for loop. It just prints four "None"










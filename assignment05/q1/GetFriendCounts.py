# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #5 Question #1

import xml.etree.ElementTree as ET


tree = ET.parse('testxmlfile2.xml')
root = tree.getroot()
# print()
# print(root.tag)
# print()
# print(root.attrib)
# print()
# print(dir(root))

# for child in root:
#    print(child.tag, child.attrib)

namespace = '{http://graphml.graphdrawing.org/xmlns}'

node = root.findall(namespace + 'graph/' + namespace + 'node')
# print(node)
# print(dir(content))

name = node[0].attrib.get('id')
# print(name)
data1 = node[0].findall(namespace + 'data')
# data2 = node[0].findall(namespace + 'data')
print(data1[1].text + ',' + data1[3].text)

# uid = person.attrib.get('uid')
# print(uid)

# name = person.find('name/first')
# middle_name = person.find('name/middle')
# last_name = person.find('name/last')

# address = person.find('address')
# street = address.find('street')
# state = address.find('state')
# city = address.find('city')
# zipcode = address.find('zip')

# print('id: ' + person.attrib.get('id'))
# print('id: ' + person.attrib.get('id'))
# print('first name: ' + first_name.text)
# print('middle name: ' + middle_name.text)
# print('last name: ' + last_name.text)
# print('street: ' + street.text)
# print('state: ' + state.text)
# print('city: ' + city.text)
# print('zip code: ' + zipcode.text)

# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #5 Question #1

import xml.etree.ElementTree as ET


content = ET.parse('testxmlfile.xml')

person = content.find('person')

first_name = person.find('name/first')
middle_name = person.find('name/middle')
last_name = person.find('name/last')

address = person.find('address')
street = address.find('street')
state = address.find('state')
city = address.find('city')
zipcode = address.find('zip')

print('id: ' + person.attrib.get('id'))
print('first name: ' + first_name.text)
print('middle name: ' + middle_name.text)
print('last name: ' + last_name.text)
print('street: ' + street.text)
print('state: ' + state.text)
print('city: ' + city.text)
print('zip code: ' + zipcode.text)

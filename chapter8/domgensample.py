#Generating XML with DOM -Chapter 8- domgensample.py

from xml.dom import minidom, Node

doc = minidom.Document()
doc.appendChild(doc.createComment('Sample XML Document - Chapter 8'))
#Generate the book

book = doc.createElement('book')
doc.appendChild(book)

#The title
title = doc.createElement('title')
title.appendChild(doc.createTextNode('Sample XML Thing'))
book.appendChild(title)

#The author section
author = doc.createElement('author')
book.appendChild(author)
name = doc.createElement('name')
author.appendChild(name)
firstname = doc.createElement('first')
name.appendChild(firstname)
firstname.appendChild(doc.createTextNode('Benjamin'))
lastname = doc.createElement('last')
name.appendChild(lastname)
lastname.appendChild(doc.createTextNode('Smith'))

affiliation = doc.createElement('affiliation')
author.appendChild(affiliation)
affiliation.appendChild(doc.createTextNode('Springy Widges, Inc.'))

#The chapter
chapter = doc.createElement('chapter')
book.appendChild(chapter)
chapter.setAttribute('name', '1') #这好像不能用int类型，必须用'1'
title = doc.createElement('title')
chapter.appendChild(title)
title.appendChild(doc.createTextNode('First Chapter'))

para = doc.createElement('para')
chapter.appendChild(para)
para.appendChild(doc.createTextNode('I Think widgets are great. You should buy it'))

company = doc.createElement('company')
para.appendChild(company)
company.appendChild(doc.createTextNode('Springy Widgets, Inc'))

para.appendChild(doc.createTextNode('.'))
print(doc.toprettyxml(indent=' '))
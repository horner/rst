#!/usr/bin/env python
from rst import rst

def main():
    doc = rst.Document('Title of the report')
    para = rst.Paragraph('Just another paragraph. We need few more of these.')
    doc.add_child(para)
    sec = rst.Section('Another', 2)
    doc.add_child(sec)
    para = rst.Paragraph('Can we do this? Yes we can.')
    doc.add_child(para)

    blt = rst.Orderedlist()
    blt.add_child('Red Hat')
    blt.add_child('Fedora')
    blt.add_child('Debian')

    doc.add_child(blt)

    sec2 = rst.Section('Why Python is awesome?', 2)
    doc.add_child(sec2)

    tbl = rst.Table('My friends', ['Name', 'Major Project'])
    tbl.add_child(('Ramki', 'Python'))
    tbl.add_child(('Pradeepto', 'Kde'))
    tbl.add_child(('Nicubunu', 'Fedora'))
    doc.add_child(tbl)

    print doc.get_rst()

if __name__ == '__main__':
    main()
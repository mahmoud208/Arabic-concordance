import codecs
import csv
import re
l=[]
l2=[]
l3=[]
with codecs.open('file.csv', 'r', encoding='utf-8') as file:
  input_file = csv.reader(file, delimiter="\t", quotechar='|')
  for row in input_file:
      text=row[0]
      text=text[1:-3]
      l.append(text[0])
      l2.append(text[2])
      l3.append(text[4])
      
      print text
for x in l2:
    print x

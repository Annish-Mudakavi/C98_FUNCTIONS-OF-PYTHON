def countwordfromfile():
     filename=input("ENTER YOUR FILE NAME")
     file=open(filename,'r')
     noofwords=0
     for x in file:
           words=x.split()
           noofwords=noofwords+len(words)
     print(noofwords)

countwordfromfile()
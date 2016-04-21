"""
Rahul Shah
11/17/15
FileChanger.py
Reads in a file and writes a new file
Changes all of the m's to M's and M's to m's
"""
#open a file to write to
f = open('newMs.txt', 'w')

#Open the document to be read 
with open("KLSadd.tex") as file:
   #loop that gets every word in file
    for word in file:
       #inside that word, gets every character
       for ch in word:
             #Change lowercase m's to capital M's and vice versa
            if(ch == "m"):
               f.write("M")
               
            elif(ch == "M"):
                f.write("m")
                
            else:
                f.write(ch)
#still don't know why I need to do this, I think this saves the file?
#If I don't, my tests show the program runs but the file stays blank when opened
f.close()


#end of FileChanger.py

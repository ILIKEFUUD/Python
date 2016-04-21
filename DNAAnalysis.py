"""
Rahul Shah
DNAAnalysis.py
Compares arrays of DNA sequences
"""


testStrand = ["A","T","T","A","G","A","C","A","T","G","G","A","G","T","T","A","C","C","A","T"]

targetStrand = ["A","T","A","A","G","A","C","A","A","C","G","A","G","A","T","A","C","C","A","T"]

#print out strands
temp = "Test Strand: "
for i in testStrand:
    temp+= i
print(temp)

temp = "Target Strand: "
for i in targetStrand:
    temp+= i
print(temp)

print("---------------------------------------------------\n")

"""
Psuedocode to find similarity

for every element in testStrand, check if
the corresponding element in targetStrand is
equal to it. If it is, increase similarity.
Once every element is checked, divide the
number of similarities by the total number
of elements and multiply by 100 to get
the percentage of similarity
"""

#calculate similarity
same = 0

for i in range(0, len(testStrand)):
    if testStrand[i] == targetStrand[i]:
        same +=1
percent = same/len(testStrand)

#output similarity
print("Similarity: ",percent*100,"%")

print("---------------------------------------------------\n")

"""
Psuedo code to create complementary strand for testStrand

Make a new array(or list)
iterate through testStrand
if element is A then append T
T append A
C append G
G append C
print
"""

#complementary strand
compStrand = []

for i in range(0,len(targetStrand)):
    base = testStrand[i]
    if(base == 'A'):
        compStrand.append('T')
    elif(base == 'T'):
        compStrand.append('A')
    elif(base == 'C'):
        compStrand.append('G')
    else:
        compStrand.append('C')

#output compStrand and testStrand
temp = "Test Strand: "
for i in testStrand:
    temp+= i
print(temp)

temp = "Complementary Strand: "
for i in compStrand:
    temp += i
print(temp)

print("---------------------------------------------------\n")

#BONUS find GGA

#output compStrand and testStrand
temp = "Test Strand: "
for i in testStrand:
    temp+= i
print(temp)

find = ""
for i in testStrand:
    find+=i
print("Search Target: GGA")
if 'GGA' in find:
    print("FOUND!")
else:
    print("NOT FOUND")






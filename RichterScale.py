"""
Rahul Shah
RichterScale.py
12/7/15
read in seismic rating, display damage level
"""

#prompt user for seismic rating
seismicRating = input("Enter seismic rating: ")
rating = float(seismicRating)
if(rating >= 8):
    print("Most structures fall")
elif(rating <8 and rating >=7.0):
    print("Many buildings destroyed")
elif(rating < 7.0 and rating >=6.0):
    print("Many buildings considerably damaged, some collapse")
elif(rating < 6.0 and rating >= 4.5):
    print("Damage to poorly constructed buildings")
elif(rating < 4.5 and rating >=3.5):
    print("Felt by many people, no destruction.")
elif(rating < 3.5 and rating >=0):
    print("Generally not felt by people")
else:
    print("Negative numbers are actually possible and recorded, but for the sake of the program, they are invalid")
    print("At the time the Richter Scale was made, it was based logarithmically on the smallest earthquakes we could observe")
    print("As technology got better and since the scale was logarithmic, negative values are correct but VERY TINY, so chill out bruh.")
    

import random

print ("Random number with seed 30")
random.seed( 30 )
print ("first - ", random.randint(25,50))
#will generate a same random number as previous
random.seed( 25 )
print ("Second - ", random.randint(25,50))
#will generate a same random number as previous
random.seed( 15 )
print ("Third - ", random.randint(25,50))
import school_scores
records_list = school_scores.get_all()
#print(records_list[0])
#print(records_list[0]['State'])
#print(records_list[0]['Year'])
#print(records_list[0]['Gender'])
#print(records_list[0]['GPA'])

#print total number of test takers
for row in records_list:
    print(row['State']['Name'], row['Year'])
   
    
    
#print(records_list[][])
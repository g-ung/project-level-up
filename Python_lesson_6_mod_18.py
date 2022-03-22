# AI Porgamming with Python: Lesson 6 Scrypting, Module 18: Reading and Writing Files

## flying circus cast list
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('/Users/gabe_ung/Desktop/flying_circus_cast.txt') as f:
    #use the for loop syntax to process each line
    ## list comprehension
        cast_list = [line.split(",")[0] for line in f] # use index[0] to extract only the names from the file
        
    ## for loop version for practice
    
        for line in f:
            contents = line.split(",")[0]
            # print(line.split(",")) # creates list of each line
            # check with print(line.split(",")[0]) # use indext of [0] to reference the extraction of the first element within list
    #and add the actor name to cast_list
            cast_list.append(contents)
        
        
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
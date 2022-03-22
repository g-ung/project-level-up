# AI Porgamming with Python: Lesson 6 Scrypting, Module 18: Reading and Writing Files

## flying circus cast list
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('/Users/gabe_ung/Desktop/flying_circus_cast.txt') as f:
        contents = f.readlines()
        print(contents)
    #use the for loop syntax to process each line
        for line in contents:
           line.split()
           print(line)
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
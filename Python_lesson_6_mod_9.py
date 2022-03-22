# AI Porgamming with Python: Lesson 6 Scripting, Module 9: Generate Messages

## generate messages
names =  input("Please enter name(s) seperated by commas: ").title().split(",") # get and process input for a list of names
assignments =  input("Please enter the assignment(s) count seperated by commas: ").split(",") # get and process input for a list of the number of assignments
grades =  input("Please enter grade(s) separated by commas: ").split(",") # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

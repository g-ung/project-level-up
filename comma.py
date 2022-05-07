'''
my_list = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string 
with all the items separated by a comma and a space, with and inserted before 
the last item. For example, passing the previous spam list to the function 
would return 'apples, bananas, tofu, and cats'. But your function should be 
able to work with any list value passed to it. Be sure to test the case where 
an empty list [] is passed to your function.
'''
def comma(some_list):
  # for loop, string.find() approach
  some_list.insert(3, 'and')
  some_list.insert(3, ',')
  string = ""
  for i in some_list:
    string += i + " "
  
  index = string.find(',')
  string_final = string[:index-1] + '' + string[index:]

  return print(string_final)
  
my_list = ['apples', 'bananas', 'tofu', 'cats']
# my_list = []
comma(my_list)


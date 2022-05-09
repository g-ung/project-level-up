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
  # join() approach
  if len(some_list) <= 2:
    return print(" and ".join(some_list))
  else:
    return print("{}, and {}".format(', '.join(some_list[:-1]), some_list[-1]))
   
my_list = ['apples', 'bananas', 'tofu', 'cats']
comma(my_list)


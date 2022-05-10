'''
Automate the Boring Stuff with Python: Comma Code

Say you have a list value like this:
my_list = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string 
with all the items separated by a comma and a space, with and inserted before 
the last item. For example, passing the previous spam list to the function 
would return 'apples, bananas, tofu, and cats'. But your function should be 
able to work with any list value passed to it. Be sure to test the case where 
an empty list [] is passed to your function.
'''
def comma(some_list):
  # join() approach with format() to build final string
  '''
  Use len() to find the number of items in some_list, now len(some_list) == x no. of 
  tiems in some_list. So if there are two (2) items in the list value, then
  len(some_list) == 2, i.e. some_list is less than or equal to 
  two then run this block of code
  REFERENCE:
  https://www.programiz.com/python-programming/methods/built-in/len
  
  '''
  if len(some_list) <= 2:
    result = " and ".join(some_list) # use join() to build your string with "and" between each string
  else:
    '''
    Use slice() to extract the items you want in some_list, then use format() and join() to 
    build the desired string output according to the requirements above.  Here, 'and' is always
    a constant and can be included as part of the format of the final string.  Use join() with
    ',' delimiter and slice() isolate the items in some_list with format() to build the string,
    i.e. some_list[:-1] == extract all items in some_list from 0 to 2nd last item
    REFERENCE:
    slice
    https://www.programiz.com/python-programming/methods/built-in/slice
    format
    https://www.programiz.com/python-programming/methods/built-in/format

    '''
    result = "{}, and {}".format(', '.join(some_list[:-1]), some_list[-1])
  
  return print(result)
   
my_list = ['apples', 'bananas', 'tofu', 'cats']
comma(my_list)


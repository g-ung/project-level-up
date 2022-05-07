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
#my_list = []
comma(my_list)


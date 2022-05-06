def comma(some_list):
  # join() list, slice approach
  some_list.insert(3, 'and')  
  string_final = " ".join(some_list)
  string_final = string_final[:19] + ',' + string_final[19:-1]

  return print(string_final)

def comma_one(some_list):
  # for loop, string.find() approach
  string = ""
  for i in some_list:
    string += i + " "
  
  index = string.find('cats')
  string_final = string[:index-1] + ', and ' + string[index:]

  return print(string_final)
  
my_list = ['apples', 'bananas', 'tofu', 'cats']
comma_one(my_list)


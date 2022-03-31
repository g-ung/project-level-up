# AI Porgamming with Python: Lesson 4 Control Flow, Module 34: Zip Coordinates; Zip Lists a Dictionary; Unzip Tuples; Transpose with Zip; Enumerate
## Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord): # point is the loop variable zipped into tubles of labels, x_coord, y_coord, z_coord
    points.append("{}: {}, {}, {}".format(*point)) # unpack the zip using *point in specified format and append to points list
    
for point in points: # iterate through unpacked list of tuples from first for loop where points is mapped points list of tuples
    print(point)

## zip to list a dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print("\n", cast)

## zip list to a dictionary
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print("\n", names)
print(heights)

## transpose with zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data)) # replace with your code
print("\n", data_transpose)

## enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for index, actor in enumerate(cast): # index and actor are mapped to cast list
    cast[index] = actor + " " + str(heights[index]) # index used to map cast to heights list, actor loop variable is mapped to cast list

print("\n", cast)
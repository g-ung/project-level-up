'''
Character Picture Grid
REQUIREMENTS:
1. Convert the grid value of 'grid' to print the image:

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

2. Use a loop in a loop to print grid[0][0], then grid[1][0], then grid[2]
[0], and so on, up to grid[8][0] to prin the first row, then print a newline
3. Then, pring grid[0][1], then grid[1][1], then grid[2][2], and so on. The
last thing your program will print is grid[8][5]

NOTE: Remember to pass the end=' ' keyword arguement to print() if you don't want
a newline printed automatically after each print() call
'''
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# grid[0][0] == top left hand corner of the grid, i.e. grid[x_axis][y_axis]
'''
transposed = zip(*grid) # use zip to transpose grid

# for loop approach to transpose x, y axis
for y_axis in range(len(grid[0])): # prints the number of items in grid[0], i.e. the first list
    for x_axis in grid: # prints the number of lists in grid
        print(x_axis[y_axis], end='')
    print()

# zip approach to reduce to single for loop
for x_axis in zip(*grid):
    print(''.join(x_axis)) # use join() to convert list to string
'''
# list comprehension approach with join() to convert grid value to string
print('\n'.join(''.join(x_axis) for x_axis in zip(*grid)))


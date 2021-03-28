CELL_SIZE = 6

def print_horizontal_line(size):
    print('_' * ((size +1) * (CELL_SIZE+2)+1))

def print_multiplication_table(size):
    print_horizontal_line(size) # first line of the table
    print('|',' '*CELL_SIZE, end='')
    for col in range(size):
        spaces = ' ' * (CELL_SIZE - len(str((col+1))))
        print('|',col+1, end=spaces) 
    print('|')   
    print_horizontal_line(size)
    for row in range(size):
        spaces = ' ' * (CELL_SIZE - len(str((row+1))))
        print('|', row+1, end=spaces)
        for col in range(size):
            spaces = ' ' * (CELL_SIZE - len(str((row + 1) * (col+1))))
            if (col<row+1):
                print('|',(row + 1) * (col+1), end=spaces)
            else:
                spaces = ' ' * (CELL_SIZE+1)
                print('|', end=spaces)
        print('|')        
        print_horizontal_line(size)


if __name__ == '__main__':
    print_multiplication_table(5)
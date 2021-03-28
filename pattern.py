### pattern
# 1
# 4 6
# 9 11 13
# 17 19 21 23

def other():
    rows = 4
    inc = 1
    seq3 = 1 
    seq1 = 1
    for row in range(rows): # manage the col sequence, seq1 = 1, 4, 9, 17, ...
        seq3 = seq3 + inc # seq 3 is used to calculate the numbers on seq1
        inc += 1
        seq2 = seq1 # sequence 2 is the sequence in a row, we get that sequence by adding 2 to the previous term
        for col in range(row+1): # this for-loop will print the row sequece
            print (seq2, end=' ')
            seq2 = seq2 + 2
        print('')
        seq1 = seq1 + seq3 + 1 # new element on the sequence that represents the first element
                            # of each row, we increment the number by using seq3 + 1
    


def print_row(row, first_value):
    seq = first_value 
    for col in range(row+1): 
        print (seq, end=' ')
        seq = seq + 2
    print('')


def pattern(rows): # rows is the number of rows we want to print
    start = 1 # this is the sequence 1 4 9 17
    aux_sequence = 2  # this is the sequence 3 5 8 12
    inc = 1 # This is used to calculate each element of the auxiliar sequence
            # for the next value, you have to add 1 to the difference of the previous two values
    for row in range(rows):  
        aux_sequence += inc # seq 3 is used to calculate the numbers on the main sequence
        inc += 1  
        print_row(row, start)
        
        start += aux_sequence  # new element on the sequence that represents the first element
                            # of each row, we increment the number by using seq3 + 1    

if __name__=='__main__':
   pattern(5)
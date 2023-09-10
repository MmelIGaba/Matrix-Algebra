## This is matrix calculator                                        v2.0 this version will only deal with just 2 matrices max per calulation

number_of_matrices = int(input('Enter the number of matrices involved in this calculation cycel: '))
rows = int(input('Enter the number of rows: \n'))
col = int(input('Enter the number of columns: \n'))
## assert
A = []
B = []
C = []

if (number_of_matrices>2):

    for i in rows:
        for j in col:
            y = float(input(f'Enter the {i}{j}th value'))
    print(y)
    
  
        
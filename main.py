## Matrix Algebra                                          by Mmela Dyantyi
## v1.0
a_11, a_12 ,a_21, a_22 = 12, 23, 34, 3  # values in the A matrix
b_11, b_12, b_21, b_22 = 5, 3, 1, 7     # values in the B matrix

A = f'{[ a_11, a_12 ,a_21, a_22]}'           # A matrix
B = f'{[b_11, b_12, b_21, b_22]}'            # B matrix
print('The A Matrix is \n',A)
print('The B matrix is \n', B)

def add(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
    
    c_11 = a_11 + b_11
    c_12 = a_12 + b_12
    c_21 = a_21 + b_21
    c_22 = a_22 + b_22
    add_A_to_B = f'A + B = {[c_11,c_12, c_21,c_22]}'
    return print(add_A_to_B)

def subtr(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
    
    c_11 = a_11 - b_11
    c_12 = a_12 - b_12
    c_21 = a_21 - b_21
    c_22 = a_22 - b_22
    subtr_A_to_B = f'A - B = {[c_11,c_12, c_21,c_22]}'
    return print(subtr_A_to_B)

   
def mult(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
    c_11 = a_11*b_11 + a_12*b_21
    c_12 = a_11*b_12 + a_12*b_22
    c_21 = a_21*b_11 + a_22*b_21
    c_22 = a_21*b_12 + a_22*b_22
    mult_A_to_B = f'A by B = {[c_11,c_12, c_21,c_22]}'
    return print(mult_A_to_B)
        
def transpose(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
    
    temp = a_12 
    a_12 = a_21
    a_21 = temp
    temp = b_12 
    b_12 = b_21
    b_21 = temp
    A = f'{[ a_11, a_12 ,a_21, a_22]}'           # A transpose
    B = f'{[b_11, b_12, b_21, b_22]}'            # B transpose 
    return print('The transpse of A is \n', A, '\n', 'The transpose of B is \n', B)

def det(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
     detA = a_11*a_22 - a_12*a_21
     detB = b_11*b_22 - b_12*b_21
     return print(f'The determinant of matrix A is {detA}', f'The determinant of matrix B is {detB}')
def inverse(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22):
    temp = -a_12
    a_12 = -a_21 
    a_21 = temp
    temp = -b_12
    b_12 = -b_21
    b_21 = temp
    A = f'A inverse is {[ a_11, a_12 ,a_21, a_22]}'           # A inverse 
    B = f'B inverse is {[b_11, b_12, b_21, b_22]}'            # B inverse 
    return print(A, B)
    
add(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
subtr(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
mult(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
transpose(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
det(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
inverse(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
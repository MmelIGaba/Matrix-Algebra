## Matrix Algebra                                          by Mmela Dyantyi
a_11, a_12 ,a_21, a_22 = 12, 23, 34, 3  # values in the A matrix
b_11, b_12, b_21, b_22 = 5, 3, 1, 7     # values in the B matrix

A = f'Matrix A is {[ a_11, a_12 ,a_21, a_22]}'           # A matrix
B = f'Matrix B is {[b_11, b_12, b_21, b_22]}'            # B matrix
print(A, '\n', B)

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
    subtr_A_to_B = f'A + B = {[c_11,c_12, c_21,c_22]}'
    return print(subtr_A_to_B)
    
add(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
subtr(a_11, a_12 ,a_21, a_22, b_11, b_12, b_21, b_22)
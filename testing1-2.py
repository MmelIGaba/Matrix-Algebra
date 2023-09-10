
a_11, a_12 ,a_21, a_22 = 12, 23, 34, 3  # values in the A matrix
b_11, b_12, b_21, b_22 = 5, 3, 1, 7     # values in the B matrix

A = [ a_11, a_12 ,a_21, a_22]         # A matrix
B = [b_11, b_12, b_21, b_22,8]          # B matrix
def add():
    C = []
    
    for i in range(max(len(A),len(B))):
        while(len(A)!=len(B)):
            if (len(A)>len(B)):
                B.append(0)
            elif (len(A)<len(B)):
                B.append(0)
        c = A[i]+B[i]
        C.append(c)
    return print(C)
add()
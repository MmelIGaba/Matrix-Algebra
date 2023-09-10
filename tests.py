num = 2
rows = 2
col = 2
A = []
B = []
def matrices():
    if num==1:
        for i in range(rows):
            for j in range(col):
                a = float(input(f'Enter the a_{i+1}{j+1} \n'))
                A.append(a)
    else:
        for i in range(rows):
            for j in range(col):
                a = float(input(f'Enter the a_{i+1}{j+1} \n'))
                A.append(a)
        for i in range(rows):
            for j in range(col):
                b = float(input(f'Enter the b_{i+1}{j+1} \n'))
                B.append(b)    
    return print(A, B)
def add(matrices):
    # bigger = A.length > B.length
    C = []
    for i in range(len(A)):
        c = A[i]+B[i]
        C.append(c)
        
    return print(C)

matrices()
add(matrices)
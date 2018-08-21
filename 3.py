import numpy as np 

def gauss_elimination(A = [], b = []):
    B = np.concatenate((A,b), axis = 1)
    n = len(B)
    B = B.astype(float)
    
    for i in range(n):
        for j in range(i):
            B[i] = B[i] - (B[j]*B[i][j]/B[j][j])
    
    for i in range(n):
        B[i] = B[i] * (1/B[i][i])

    for i in reversed(range(n-1)):
        for j in range(n-i-1):
            B[i] = B[i] - B[i][n-j-1]*B[n-j-1]
    
    return B[:, 4] 

print(gauss_elimination([[3, 4, 2, 7], [7, 5, 1, 9], [8, 12, 25, 3], [9, 11, 15, 7]], 
                [[129], [151], [709], [505]]))
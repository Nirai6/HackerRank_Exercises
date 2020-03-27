def hourglass(matrix):
    maximum=-63
    for i in range(0,4):
        for j in range(0,4):
            s=matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
            maximum= (max(s,maximum))
    return maximum
    
                

n=6
mat=[]
for i in range(n):
    elements=[list(map(int,input().rstrip().split()))][:n]
    mat.extend(elements)
maximum=hourglass(mat)
print(maximum)

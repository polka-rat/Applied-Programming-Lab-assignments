def convolve(A, B):
    C=[0]*(len(A)+len(B)-1)
    for i in range(len(C)):
        k=0
        while i-k>=0:
            if i-k<len(B) and k<len(A):
                C[i]+=A[k]*B[i-k]
            k+=1
    return C


def rectangles_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    rect1=[(x1,y1),(x1,y1+h1),(x1+w1,y1),(x1+w1,h1+y1)]
    rect2=[(x2,y2),(x2,y2+h2),(x2+w2,y2),(x2+w2,h2+y2)]
    
    for i in rect1:
        if i[0]<=max(x2+w2,x2) and i[0]>=min(x2,x2+w2):
            if i[1]<=max(y2,y2+h2) and i[0]>=min(y2,y2+h2):
                return "Overlap"
            
    for i in rect2:
        if i[0]<=max(x1+w1,x1) and i[0]>=min(x1,x1+w1):
            if i[1]<=max(y1,y1+h1) and i[0]>=min(y1,y1+h1):
                return "Overlap"
        
    return "No overlap"

from collections import defaultdict

def sudoku_check(grid):
    inv=0
    

    
    blocks=defaultdict(lambda: defaultdict(int))
    rows=defaultdict(lambda: defaultdict(int))
    
    k=0
    while k<3:
        m=0
        while m<9:
            rows[k][grid[k][m]]+=1
            if m<3:
                blocks['block1'][grid[k][m]]+=1                
            elif m<6 and m>=3:
                blocks['block2'][grid[k][m]]+=1
            else:
                blocks['block3'][grid[k][m]]+=1
            m+=1
        k+=1
     
    while k<6:
        m=0
        while m<9:
            rows[k][grid[k][m]]+=1
            if m<3:
                blocks['block4'][grid[k][m]]+=1                
            elif m<6 and m>=3:
                blocks['block5'][grid[k][m]]+=1
            else:
                blocks['block6'][grid[k][m]]+=1
            m+=1
        k+=1
     

    while k<9:
        m=0   
        while m<9:
            rows[k][grid[k][m]]+=1
            if m<3:
                blocks['block7'][grid[k][m]]+=1                
            elif m<6 and m>=3:
                blocks['block8'][grid[k][m]]+=1
            else:
                blocks['block9'][grid[k][m]]+=1
            m+=1
        k+=1
         
    li=[list(x[1].values()) for x in blocks.items()]   
    li=list(filter(lambda x: max(x)>1, li))
    inv+=len(li)
    
    lj=[list(x[1].values()) for x in rows.items()]   
    # print(lj)
    lj=list(filter(lambda x: max(x)>1, lj))
    # print(lj)
    inv+=len(lj)
            
    gridt = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    
    lk=[list(set(x)) for x in gridt]
    lk=list(filter(lambda x: len(x)<9,lk))
    # print(lk)
    inv+=len(lk)
    return inv

    # li=[list(set(x)) for x in grid]
    # lj=filter(lambda x: len(x)<9,li)
    # inv+=len(lj)
    
    #transpose

        
A=[3,2,5,6]
B=[1,2,4]
# print(convolve(A,B))

# print(rectangles_overlap(0, 0, 2, 2, 1, 1, 2, 2))


	
sblk = [
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2, 3, 4, 5, 6, 7, 8, 9, 1],
 [3, 4, 5, 6, 7, 8, 9, 1, 2],
 [4, 5, 6, 7, 8, 9, 1, 2, 3],
 [5, 6, 7, 8, 9, 1, 2, 3, 4],
 [6, 7, 8, 9, 1, 2, 3, 4, 5],
 [7, 8, 9, 1, 2, 3, 4, 5, 6],
 [8, 9, 1, 2, 3, 4, 5, 6, 7],
 [9, 1, 2, 3, 4, 5, 6, 7, 8]
]
# print(sudoku_check(sblk))

# print('Hello ' + 'World')

def palin(n):
    s = [int(x) for x in str(n)]
    
    # First check if already palindrome - then inc by 1
    lmid = (len(s)+1) // 2 -1
    mid  = (len(s) + 1) // 2 - 1
    p = True

    for i in range(lmid+1):
        if s[i] != s[-i-1]:
            p = False
            break
    if p:
        s = [int(x) for x in str(n+1)]

    # print(s[:lmid+1])
    # print(s[:-(lmid+2):-1])
    if s[:lmid+1] < s[:-(lmid+2):-1]:
        s[mid] += 1

    for i in range(lmid+1):
        s[-i-1] = s[i]
    
    return int(''.join([str(x) for x in s]))

print(palin(101))
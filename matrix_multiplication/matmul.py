#Assignment 1 - Matrix Multiplication

#Date: 10.8.24
#Name: Deepak Charan S
#Roll No: EE23B022

#Description: To implement matrix multiplication. Our code should also have check against invalid matrix entries and displaying the appropriate errors

def matrix_multiply(mat1 : list[list], mat2 : list[list]) -> list[list]:
    row1=len(mat1)  #Getting the number of rows of both the matrices
    row2=len(mat2)    
    
    if row1==0 or row2==0:  #checking if matrix is empty
        raise ValueError("Matrix is Empty!!")
    
    
    if not isinstance(mat1[0], (list,tuple)) or not isinstance(mat2[0], (list,tuple)):  #the rows of the matrix must be only a list/tuple
        raise TypeError("Invalid Matrix")
    else:
        col2=len(mat2[0])  
        col1=len(mat1[0])
        
    if col1==0 or col2==0:  #checking if matrix is empty (matrix might be represented as [[]] which would give row!=0)
        raise ValueError("Matrix is Empty!!")    
    
    
    #Performing the same sanity checks throughout all the rows of both the matrices
    for i in mat1:          
        if not isinstance(i, (list,tuple)) or not isinstance(i, (list,tuple)):
            raise TypeError("Invalid Matrix")
        if len(i)!=col1:
            raise ValueError("Matrix Is Invalid")
    
    for i in mat2:
        if not isinstance(i, (list,tuple)) or not isinstance(i, (list,tuple)):
            raise TypeError("Invalid Matrix")
        if len(i)!=col2:
            raise ValueError("Matrix Is Invalid")
     
        
    if col1!=row2:  #A must condition if we have to perform multiplication
        raise ValueError("Dimensions dont match! Cant perform multiplication.")


    mat_fin=[]  #final matrix
            
    for i in range(row1): 
        mat_fin.append([])  #creating a row for the matrix
        for j in range(col2):
            sum=0
            for k in range(col1):
                if isinstance(mat1[i][k], (int, float,complex)) and isinstance(mat2[k][j], (int, float,complex)):   #to check for invalid data types
                    sum+=mat1[i][k]*mat2[k][j]
                else:
                    raise TypeError("Matrix Has Invalid Datatypes")
            mat_fin[i].append(sum)  
    
    return mat_fin  #returning the final matrix
        
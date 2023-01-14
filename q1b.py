import numpy as np

def manipulateMatrix(matrix):
    print("##### Absolute Matrix #####\n",np.abs(matrix))
    
    print("###### Negative Values #####\n",matrix[np.where(matrix<0)])
    
    addColAndRow(matrix)
    removeColAndRow(matrix,2,3)
    matrix = np.abs(matrix)
    maximum,minimum = np.max(matrix),np.min(matrix)
    print("Maximum value in absolute matrix ==> ",maximum)
    print("Minimum value in absolute matrix ==> ",minimum)

    print("Sum of all elements in absolute matrix ==> ",np.sum(matrix))

def addColAndRow(matrix):
    matrix2 = np.abs(np.round_(np.random.randn(5,6) * 10,decimals=2))
    print("##### Matrix2 #####\n",matrix2)

    x1,y1 = np.shape(matrix)
    x2,y2 = np.shape(matrix2)

    # adding a column using insert method
    newmatrix = np.insert(matrix,y1,matrix2[:,x2-1],axis=1)
    
    # adding a rows using append method
    newmatrix = np.vstack((newmatrix,matrix2[x1-1]))

    # note last rows and columns are added to the matrix

    print("##### New Matrix  #####\n",newmatrix)

def removeColAndRow(matrix,row,col):
    print("##### Matrix #####\n",matrix)
    newmatrix2 = np.delete(matrix,row,axis=0)
    newmatrix2 = np.delete(newmatrix2,col,axis=1)
    print(f"#### Removing {row+1} row And {col+1} column ####\n",newmatrix2)


if __name__ == "__main__":
    # created a sample matrix rrounding off to 2 decimal places and then multiplying the values by 10
    matrix = np.round_(np.random.randn(5,5) * 10,decimals=2)
    print("##### Matrix #####\n",matrix)
    manipulateMatrix(matrix)
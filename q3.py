import numpy as np

def createMatrices():
    matrix1 = np.random.randint(20,50,size=(5,5))
    matrix2 = np.random.randint(20,50,size=(5,5))
    print("Matrix1\n",matrix1,"\n\nMatrix2\n",matrix2)

    print("\nAddition of Matrices")
    addMatrices(matrix1,matrix2)

    print("\nSubtraction of Matrices")
    subMatrices(matrix1,matrix2)

    print("\nMultiplication of Matrices")
    mulMatrices(matrix1,matrix2)

    print("\nDivision of Matrices")
    divMatrices(matrix1,matrix2)

def addMatrices(m1,m2):
    additionMatrix = np.array(m1) + np.array(m2)
    print(additionMatrix,"\n")

def subMatrices(m1,m2):
    subtractionMatrix = np.array(m1) - np.array(m2)
    print(subtractionMatrix)

def mulMatrices(m1,m2):
    multiplicationMatrix = np.array(m1) * np.array(m2)
    print(multiplicationMatrix)

def divMatrices(m1,m2):
    divisionMatrix = np.array(m1) / np.array(m2)
    print(divisionMatrix)


def showRows(matrix,row):
    print(f"{row} Row of Matrix ==> {matrix[row]} ")

def showCols(matrix,col):
    print(f"{col} Col of Matrix : {matrix[:,col]}")

if __name__ == "__main__":
    createMatrices()
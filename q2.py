import numpy as np
# Part (a)
def getData():
    # file opening , reading the values
    with open("sample.txt") as matrixData:
        for line in matrixData.readlines():
            data,dim = line.replace("\n","").split("@")
            rows,cols = int(dim[0]),int(dim[2])
            # creating matrix according to the data
            createMatrix(data,rows,cols)

def createMatrix(data,rows,cols):
    matrix,arr,counter,data= [],[],0,data.split(",")
    for i in range(rows):
        for j in range(cols):
            arr.append(int(data[counter]))
            counter += 1
        matrix.append(arr)
        arr = []
    print("Matrix\n",np.array(matrix))
    print("Shape ==> ",np.shape(matrix))
    size = compute(matrix)
    saveData(size,matrix)

# Part (b)
def compute(matrix):
    print("Size of matrix ==> ",np.size(matrix))
    for i in range(np.shape(matrix)[0]):
        print("Row Data ==> ",matrix[i],"\n Size of Row ==> ",len(matrix[i]))
    return np.size(matrix)
    
def saveData(size,matrix):
    with open("dataMatrix.txt","a") as fh:
        fh.writelines(f"{matrix}\nSize of Matrix {size}\n")

if __name__ == "__main__":
    getData()
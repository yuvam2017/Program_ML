import numpy as np

def createArrays():
    print("###### Arrays With all ones ##########")
    print(np.ones(shape=(5,4)))

    print("###### Arrays wiith all zeros ########")
    print(np.zeros(shape=(5,5)))
    
    print("####### Arrays with random values within range ########")
    # using int values in the np random randint fucntion 1=lower range , 100= higher range
    print("Using Int values\n",np.random.randint(1,100,size=(5,5)))

    print("Using the float values\n",np.random.randn(5,5))

    print("######## A diagonal Matrix #######")
    # data for the diagonal of the diagonal matrix
    data = [1,2,3,4,5]
    print(np.diag(v=data))
    # v stands for vector it can be 1d or 2d data 
    
if __name__ == "__main__":
    # Function to create arrays
    createArrays()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

matrix = np.random.randn(5,5)
print("Matrix \n",matrix,"\n")
sinMatrix = np.sin(matrix)
print("Sine Matrix\n",sinMatrix)

sinMatrixdf = pd.DataFrame(sinMatrix)
sinMatrixdf.plot(xlabel = "Range", ylabel = "Sine Values", title ="Line Graph")

sinMatrixdf.plot.bar(xlabel = "Index", ylabel = "Sine Values", title =
"Bar Graph")

sinMatrixdf.plot.scatter(x=2,y=3,c="red",title="Second vs Fifth Column")

cosMatrix = np.cos(matrix) 
print("\nThe Cosine Values for Matrix Data is: \n", cosMatrix)
cosMatrixdf = pd.DataFrame(cosMatrix, columns = ["First", "Second",
"Third","Fourth","Fifth"]) 
print("\nThe Cosine Values as DataFrame: \n", cosMatrixdf)

# For Pie Plot
absMat = cosMatrixdf.abs()
absMat.plot.pie(subplots=True, title = "Pie Plot", figsize=(15,5))

# For Area Plot
absMat.plot.area(xlabel = "Range", ylabel = "Cosine Values", title ="Area Plot", stacked = True)

# For Histogram
cosMatrixdf.plot.hist(title = "Histogram", stacked = True)

# Line Plot
dates= pd.date_range(start="01/01/2023",end="17/01/2023",freq="D")
share_prices =  np.random.randn(1, 17)[0]
plot.figure(figsize=(12,5))
plot.plot(dates,share_prices)
plot.title("Share Prices in The Month of January")
plot.xlabel("Dates")
plot.ylabel("Prices in dollar $")
plot.show()

# bar plot
fruits=["Apple","Guava","Banana","Mango","Coconut","Kiwi","Orange","Grapes"]
prices = [18,38,29,10,16,27,31,49]
plot.barh(fruits,prices)
plot.title("Month January Fruit Sales")
plot.ylabel("Fruits")
plot.xlabel("Weight (in Kg)")
plot.savefig("FruitSales.png")

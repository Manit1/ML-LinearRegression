import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading of data
data=pd.read_csv("headbrain (1).csv")
data.head()

#Collecting X and Y
X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

#Mean of X and Y
m_x=np.mean(X)
m_y=np.mean(Y)

#Total number of enteries
m=len(X)

#using the formula to calculate B0 and B1
numer=0
denom=0
for i in range(m):
    numer += (X[i] - m_x) *(Y[i] - m_y)
    denom += (X[i] - m_x)**2

b1= numer / denom
b0= m_y - b1*m_x
y=b0+b1*X


#plotting the graph
plt.scatter(X,Y,marker='o')
plt.plot(X,y,color="black")
plt.xlabel("Head size(cm^3)")
plt.ylabel("Brain Weight(grams)")
plt.legend()
plt.show()

size=4512
y=b0+b1*size
print(y)
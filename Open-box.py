
import csv 

#domain is 0<x<105
#we let accuracy to 5 dp, or computer will implode
x=0.00001
with open('Math AA.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Value of X", "Volume"])
    while (x<105) :
        writer = csv.writer(file)
        writer.writerow([x, ""])
        x+=0.00001


import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.7f}'.format
plt.rcParams["axes.formatter.limits"] = (-5, 12)
#Given that volume=4x^3-1014x^2+62370x
df=pd.read_csv("Math AA.csv")
count_row = df.shape[0]
def find_volume(V):
        return 4*(V**3)-1014*(V**2)+62370*V

df["Volume"]=df["Value of X"].apply(find_volume)

df.to_csv("Math AA.csv")
print(df)

df2=df.loc[df['Volume'].idxmax()]
print(df2)
df.plot(x = 'Value of X', y = 'Volume')
plt.show()
import plotly as pk
import csv
import plotly.figure_factory as pd
import pandas as pf
import statistics as st
import random


df=pf.read_csv("stuMark.csv")
ms=df["Math_score"].to_list()
fig=pd.create_distplot([df["Math_score"].to_list()],["Math_score"])
fig.show()
mean1=st.mean(ms)
print("ms: ",mean1)
std1=st.stdev(ms)
print("SD: ",std1)


dataset=[]
for i in range(0,100):
    randomindex=random.randint(0,len(ms))
    value=ms[randomindex]
    dataset.append(value)


fig2=pd.create_distplot([dataset],["dataset"])
fig2.show()
mean2=st.mean(dataset)
print(mean2)
std2=st.stdev(dataset)
print(std2)

df1=pf.read_csv("data1.csv")
ms1=df1["Math_score"].to_list()
figdata1=pd.create_distplot([df1["Math_score"].to_list()],["Math_score"])
figdata1.show()
meandata1=st.mean(ms1)
print("ms data1: ",meandata1)
stddata1=st.stdev(ms1)
print("SD data: ",stddata1)

df2=pf.read_csv("data2.csv")
ms2=df["Math_score"].to_list()
figdata2=pd.create_distplot([df2["Math_score"].to_list()],["Math_score"])
figdata2.show()
meandata2=st.mean(ms2)
print("ms2: ",meandata2)
stddata2=st.stdev(ms)
print("SD: ",stddata2)

df3=pf.read_csv("data3.csv")
ms3=df["Math_score"].to_list()
figdata3=pd.create_distplot([df3["Math_score"].to_list()],["Math_score"])
figdata3.show()
meandata3=st.mean(ms3)
print("ms: ",meandata3)
stddata3=st.stdev(ms)
print("SD: ",stddata3)

zscore=(mean2-meandata1/std2)
print(zscore)

zscore1=(mean2-meandata2/std2)
print(zscore1)

zscore2=(mean2-meandata3/std2)
print(zscore2)
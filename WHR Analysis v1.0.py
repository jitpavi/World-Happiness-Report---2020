"""
Code Name: World Happiness Report - Data Analysis
Code Author: Jitin Pavithran
Code Version: v0.1
Code Description:
"""

import seaborn as sns
import  matplotlib.pyplot as plt
import numpy as np
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import datetime

start_time = datetime.datetime.now()

year_val = datetime.datetime.now()

url_whr = "https://worldhappiness.report/ed/2020/#read"
resp_whr = requests.request('GET',url_whr)
soup_whr = BeautifulSoup(resp_whr.text,'html.parser')
soup_dwl = soup_whr.find('ul',class_='downloads')
#re_data = re.findall(r'https\:\//happiness\-report\.s3\.amazonaws\.com\/20[2-9][0-9]/WHR[2-9][0-9]\_DataForFigure[1-9]\.1\.xls',str(soup_dwl))


for s_dwl in soup_dwl:
    link_dwl = s_dwl.find('a',title="Download Data for Figure 2.1")
    #print(str(s_dwl))
    #re_data = re.findall(r'https\:\//happiness\-report\.s3\.amazonaws\.com\/20[2-9][0-9]/WHR[2-9][0-9]\_DataForFigure[1-9]\.[1-9]\.xls',str(s_dwl))
    #print(re_data)
    if link_dwl:
        link = link_dwl['href']
        break

df_whr = pd.read_excel(link)
#df_whr = pd.read_excel(re_data[0])
#df_whr.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHRRAWData.csv",index=False)

df_whr_1 = df_whr.drop(columns={'Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Ladder score in Dystopia','Dystopia + residual'},axis=1)
rows = len(df_whr_1['Country name'])

df_whr_1['Overall Rank'] = df_whr_1.index + 1
df_whr_1.set_index(keys='Overall Rank',inplace=True)
df_whr_1.rename(columns={'Regional indicator':'Region', 'Ladder score':'Happiness Score', 'Explained by: Log GDP per capita':'GDP per Capita', 'Explained by: Social support':'Social support', 'Explained by: Healthy life expectancy':'Health', 'Explained by: Freedom to make life choices':'Freedom of life', 'Explained by: Generosity':'Generosity', 'Explained by: Perceptions of corruption':'Corruption',},inplace=True)

wf_whr_grp = df_whr_1.groupby('Region').agg({'Happiness Score':'mean'})
#print(wf_whr_grp)





df_whr_corr = (df_whr_1.corr(method='spearman'))

fig0,ax0 = plt.subplots(figsize=(30,8))
plt.title("Heatmap displaying the Correlation mapping between 6 variables and Happiness Score")
sns.heatmap(df_whr_corr,vmin=-1,vmax=1,cmap="Accent",annot=True)

Z = df_whr_1[['GDP per Capita', 'Social support', 'Health', 'Freedom of life', 'Generosity', 'Corruption']]
#Z = df_whr_1[['GDP per Capita', 'Social support', 'Health','Freedom of life','Generosity']]
Y = df_whr_1['Happiness Score']

fig4,ax4 = plt.subplots(figsize=(30,8))
sns.boxplot(df_whr_1['Region'],Y,data=df_whr_1,ax=ax4)

fig1,ax1 = plt.subplots(nrows=2,ncols=3,figsize=(30,8))
fig1.canvas.set_window_title("Regression Plot showing Correlation between 6 Variables and Happiness Score")

c = df_whr_1.columns.values.tolist()
for i in range(2):
    for j in range(3):
        k= j + (i+1)*3
        sns.regplot(x=df_whr_1[c[k]], y=Y, data=df_whr_1, ax=ax1[i, j])

plt.ylim(0, )

def DistributionPlot(yactual,ypredict,redlabel,greenlabel):
    width = 12
    height = 10
    plt.figure(figsize = (width,height))

    ax = sns.distplot(yactual, hist=False, color='teal', label=redlabel, kde_kws={'shade':True,'linewidth':3})
    sns.distplot(ypredict, hist=False, color='gold', label=greenlabel,ax=ax,kde_kws={'shade':True,'linewidth':3})

    plt.title('Actual vs Predicted Values for Happiness Score')
    plt.xlabel('')
    plt.ylabel('')

from sklearn.model_selection import train_test_split

z_train,z_test,y_train,y_test = train_test_split(Z,Y,test_size=0.2,random_state=1)

print("number of test samples :", z_test.shape[0])
print("number of training samples:",z_train.shape[0])

from sklearn.linear_model import LinearRegression

whr_lr = LinearRegression()
whr_lr.fit(Z,Y)
Y_hat_whr = whr_lr.predict(Z)

L_train = LinearRegression()
L_test = LinearRegression()

L_train.fit(z_train,y_train)
L_test.fit(z_test,y_test)

Yhat_train = L_train.predict(z_train)
Yhat_test = L_test.predict(z_test)

DistributionPlot(Y,Y_hat_whr,'Actual Score','Predicted Multi-Linear Score')
DistributionPlot(y_train,Yhat_train,'Actual Score','Predicted Train Score')
DistributionPlot(y_test,Yhat_test,'Actual Score','Predicted Test Score')





df_whr_1.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHRfilterData.csv")
end_time = datetime.datetime.now()
total_time = end_time-start_time
print(total_time)

plt.show()
#plt.close()
"""
Code Name: World Happiness Report 2020 - Data Analysis
Code Author: Jitin Pavithran
Code Version: v0.1
Code Description: This code helps in identifying those list of variables which are having a strong correlation in deciding the happiness score factor for each country.
"""

# import all the important libraries
import seaborn as sns
import  matplotlib.pyplot as plt
import numpy as np
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# Compute the starttime to evaluate the total code execution time
start_time = datetime.datetime.now()

year_val = datetime.datetime.now()

# Read the url and create a Soup object for web scraping
url_whr = "https://worldhappiness.report/ed/2020/#read"
resp_whr = requests.request('GET',url_whr)
soup_whr = BeautifulSoup(resp_whr.text,'html.parser')
soup_dwl = soup_whr.find('ul',class_='downloads')

# extract the correct link which contains the data for further analysis
for s_dwl in soup_dwl:
    link_dwl = s_dwl.find('a',title="Download Data for Figure 2.1")
    if link_dwl:
        link = link_dwl['href']
        break

# Extract the data from the link and save it in a Pandas Dataframe
df_whr = pd.read_excel(link)

# Save the raw date from the dataframe in an excel sheet
df_whr.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHRRAWData.csv",index=False)

# Drop the columsn not required as a part of Data wrangling process
df_whr_1 = df_whr.drop(columns={'Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Ladder score in Dystopia','Dystopia + residual'},axis=1)
rows = len(df_whr_1['Country name'])

# Add a new column displaying the Rank for each country in ascending order
df_whr_1['Overall Rank'] = df_whr_1.index + 1
df_whr_1.set_index(keys='Overall Rank',inplace=True)

# Rename the columns in simplified form
df_whr_1.rename(columns={'Regional indicator':'Region', 'Ladder score':'Happiness Score', 'Explained by: Log GDP per capita':'GDP per Capita', 'Explained by: Social support':'Social support', 'Explained by: Healthy life expectancy':'Health', 'Explained by: Freedom to make life choices':'Freedom of life', 'Explained by: Generosity':'Generosity', 'Explained by: Perceptions of corruption':'Corruption',},inplace=True)

# Data Visualisation starts from here

# First we will try to undertstand the correlation between 6 variables
df_whr_corr = (df_whr_1.corr(method='spearman'))

#Plot a HeatMap object displaying the correlation between variables and Happiness score
fig0,ax0 = plt.subplots(figsize=(14,7))
plt.title("Heatmap displaying the Correlation mapping between 6 variables and Happiness Score")
sns.heatmap(df_whr_corr,vmin=-1,vmax=1,cmap="Accent",annot=True)
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHR-HeatMap.jpg")

# Define the input variables for Regression plot
Z = df_whr_1[['GDP per Capita', 'Social support', 'Health', 'Freedom of life', 'Generosity', 'Corruption']]
Y = df_whr_1['Happiness Score']

# Create a Figure object with dimension 2 rows and 3 columns for showing plot fo each variable
fig1,ax1 = plt.subplots(nrows=2,ncols=3,figsize=(14,7))
fig1.canvas.set_window_title("Regression Plot showing Correlation between 6 Variables and Happiness Score")
fig1.tight_layout(pad=3.0)

# Plot regression plot for each of the 6 variables
c = df_whr_1.columns.values.tolist()
for i in range(2):
    for j in range(3):
        k= j + (i+1)*3
        sns.regplot(x=df_whr_1[c[k]], y=Y, data=df_whr_1, ax=ax1[i, j])

plt.ylim(0, )
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHR-RegressionPlot.jpg")


# define a function to create Distribution plot with the input variables provided
def DistributionPlot(yactual,ypredict,redlabel,greenlabel):
    width = 12
    height = 10
    plt.figure(figsize = (width,height))

    ax = sns.distplot(yactual, hist=False, color='teal', label=redlabel, kde_kws={'shade':True,'linewidth':3})
    sns.distplot(ypredict, hist=False, color='gold', label=greenlabel,ax=ax,kde_kws={'shade':True,'linewidth':3})

    plt.title('Actual vs Predicted Values for Happiness Score')
    plt.xlabel('')
    plt.ylabel('')
    plt.savefig(rf"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHR-DistPlot-{greenlabel}.jpg")

# import train test split module
from sklearn.model_selection import train_test_split

# create variables for test train split
z_train,z_test,y_train,y_test = train_test_split(Z,Y,test_size=0.2,random_state=1)

from sklearn.linear_model import LinearRegression

# create a Multi-Linear regression Plot
whr_lr = LinearRegression()
whr_lr.fit(Z,Y)
Y_hat_whr = whr_lr.predict(Z)

# Create the Linear Regression Objects for both Trained Data and Test Data
L_train = LinearRegression()
L_test = LinearRegression()

# Fit the trained data and Test data into the MultiLinear Regression Models
L_train.fit(z_train,y_train)
L_test.fit(z_test,y_test)

# Predict values fo trained data
Yhat_train = L_train.predict(z_train)

# Predict values fo test data
Yhat_test = L_test.predict(z_test)



# Call the Distribution Plot functions for with the predicted values of different regression plot
DistributionPlot(Y,Y_hat_whr,'Actual Score','Predicted Multi-Linear Score')
DistributionPlot(y_train,Yhat_train,'Actual Score','Predicted Train Score')
DistributionPlot(y_test,Yhat_test,'Actual Score','Predicted Test Score')



# Plot a boxplot to understand the range of happiness score in each region
fig4,ax4 = plt.subplots(figsize=(14,7))
sns.boxplot(Y, df_whr_1['Region'], data=df_whr_1,ax=ax4,orient="h")
plt.title("Boxplot displaying variance of Happiness for each respective region on the World")
plt.tight_layout()
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHR-BoxPlot.jpg")

# Save the Filtered Data into a CSV file for reference
df_whr_1.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\WHR\WHRfilterData.csv")

# Compute the total execution time and print on the screen
end_time = datetime.datetime.now()
total_time = end_time-start_time
print(total_time)

#plt.show()
plt.close()
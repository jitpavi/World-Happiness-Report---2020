# Project Name -  World-Happiness-Report-2020 - Data Analysis with Python
#### -- Project Status: [Active]
Still exploring the correlation between different variable impacting the effective Happiness Score.

## Project Intro/Objective:
The purpose of this project is to understand the correlation between 6 input variables and how it largely impacts the decision of producing a Happiness Score for each Country in the world. 

### Methods Used:
* Web Scraping
* Explorative Data Analysis
* Data Wrangling
* Data Visualization
* Data Correlation
* Multi-Linear Regression models

### Technologies:
* Python
* Pandas
* Pycharm
* Matplotlib
* Beautiful Soup
* SeaBorn
* Sklearn

## Project Description

### Prerequisites: 
  ### -> Dataset:
  Access the following URL which generates world Happiness report for each country in an yearly report.(https://worldhappiness.report/ed/2020/#read)
  
  ### -> Python Libraries:
  * Pandas
  * Matplotlib
  * Beautiful Soup
  * SeaBorn
  * Sklearn
  * Linear regresion
  * train_test_split

### Workflow:
##### 1. Using web scraping method find the url which contains the WHR report.
##### 2. Convert the extracted report form the URL into Dataframe.
##### 3. Perform Data Wrangling by removing irrelevant columns and renaming the important column names in a simplified form
##### 4. Perform Spearman Correlation and understand the correlation of six different variables by plotting the Seaborn Heatmap
   As you can observe that variables like 'GDP per Capita', 'Social support' and 'Health' are strongly correlated with Score while 'Freedom of life' is having good correlation with the Score.
   
   ![WHR - HeatMap Plot](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/Output%20Images/WHR-HeatMap.jpg)

#### 5. To get a more conclusive evidence we will plot Linear regression using each of the 6 variables with the Happiness Score. 
   This exactly supportst the figure we received in the heatmap confirming the strong correlation between 'GDP per Capita', 'Social support' and 'Health' and score
   
   ![WHR - Regression Plot](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/Output%20Images/WHR-RegressionPlot.jpg)

#### 6. To get a more conclusive evidence we will plot Multilinear regression over the trained data and test data and based on the      result which will be used an input to plot Distribution Plot to verify if the Predicted values matches with the actual values:
    As you can observe Predicted values not exactly matches with the actual score over the 3 different plots
    
    ![WHR - Predicted MultiLinear Regression Plot](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/Output%20Images/WHR-DistPlot-Predicted%20Multi-Linear%20Score.jpg)

    ![WHR - Predicted Train Score](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/Output%20Images/WHR-DistPlot-Predicted%20Train%20Score.jpg)

    ![WHR - Predicted Test Score](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/Output%20Images/WHR-DistPlot-Predicted%20Test%20Score.jpg)

#### 7. Display the combine bar charts for the top 10 states with the most affected cases.

## Expected Output:
To some extent we have managed to derive a conclusive evidence that have a strong correlation in deciding the effective Happiness score in each country however there is still a need to factor in more number of input variables in deciding the Happiness Score effectively.

## Featured Notebooks/Analysis/Deliverables:

* [WHR Analysis v1.0.py](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/WHR%20Analysis%20v1.0.py)

## Versioning:

Code version - v1.1

## Authors:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://data.gov.in/major-indicator/covid-19-india-data-source-mohfw

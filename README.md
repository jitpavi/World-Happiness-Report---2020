# Project Name -  World-Happiness-Report-2020 
#### -- Project Status: [Active]
Still exploring the correlation between different variable impacting the effective Happiness Score.

## Project Intro/Objective:
The purpose of this project is to produce a combined bar chart for the top 10 states of India currently with the most affected cases of Covid-19 where each bar is displaying Total no of covid cases, Total no. of cured cases and Total no. of Deaths respectively for each states.

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
1. Using request module download the data from the govt. website.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object with columns Death,Total Confirmed cases and Cured/Discharged/Migrated.
4. Sort the dataframe by the column name Total Confirmed cases in descending order.
5. Create a fig subplot and create 3 ax objects where each representing a bar chart for the columns  Total no of covid cases, Total no. of cured cases and Total no. of Deaths respectively
6. Enable annotation on each bar denoting the number of cases.
7. Display the combine bar charts for the top 10 states with the most affected cases.

## Expected Output:

![WHR-BoxPlat image](https://github.com/jitpavi/World-Happiness-Report---2020/blob/master/WHR-BoxPlot.jpg)

* [Covid-19 Statistics.jpg](https://github.com/jitpavi/Covid-19-Cases-in-States-of-India/blob/master/Covid-19%20Statistics.jpg)

## Featured Notebooks/Analysis/Deliverables:

* [COVID-19 Cases Indian States v1.0.py](https://github.com/jitpavi/Covid-19-Cases-in-States-of-India/blob/master/COVID-19%20Cases%20Indian%20States%20v1.0.py)

## Versioning:

Code version - v1.1

## Authors:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://data.gov.in/major-indicator/covid-19-india-data-source-mohfw

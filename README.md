# Salary-Analysis-and-Prediction

* Created a tool that estimates various data science roles salaries (MAE ~ $ 25K) to help data scientists negotiate their income when they get a job.
* Scraped over 3500 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, etc. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.11.1
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Article refered:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 
*	Easy Apply

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

1) Drop Unneccessary columns
2) Make Colums in lower case
3) Remove all text after delimiter in "job title", "location", "headquarters", "revenue" and split location into state and city attributes
4) rename columns - "type of ownership" to "ownership" and "salary estimate" to "salary($)"
5) Replace unknown with NaN in "ownership"
6) Replace -1 with False in "easy apply"
7) Replace TRUE with True in "easy apply"
8) Replace -1 with NaN in "sector"
9) Replace -1 with NaN in "size"
10) Replace -1 with NaN in "founded"
11) Replace -1 with NaN in "rating"
12) Replace -1 with NaN in "company name"
13) Drop the rows containing NA and reset the indexing
14) Remove the dollor sign, 'k' and the text in "salary($)"
15) Make 3 new columns "min salary", "max salary" and "avg salary" using "salary($)"
16) Typecase the values in "founded" to int and find the "age" of the company
17) Format the "company name" attribute by removing unwanted text
18) Make an attribute to show "headquarters" is same as the city
19) Check if the job involves python, aws or excel. Even find the length of description. Then drop "job description"
20) Change "United Kingdom" in State to "UK".
21) Make a "seniority" attribute to show if the position is senior or junior - sr = senior = lead = principal and jr = junior
22) Make a "job simplification" attribute - says if the attribute involves data scientist, data engineer, machine learning, manager, director. Else NA
23) Make an attribute for number of competitors and drop the "competitors" attribute

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/bar.jpg)
![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/heatmap.jpg)
![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/pivot.jpg)
![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/hist%20of%20avg%20sal.jpg)
![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/wordcloud.jpg)

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20% and train size of 80%   
I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – With the sparsity associated with the data, I thought that this would be a good fit. 
*	**Ensembles** - Combining the best results for a better model

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 25.92
*	**Tuned Random Forest**: MAE = 26.03
*	**Multiple Linear Regression**: MAE = 25.99
*	**Lasso Regression**: MAE = 25.21
*	**Ensembles**: MAE = 25.08

I continued to use Lasso Regression for simplicity and it gave a better result compared to Random Forest and Multiple Linear Regression

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/wsgi.jpg)
![alt text](https://github.com/raghavan93513/Salary-Analysis-and-Prediction/blob/main/Screenshots/Salary%20Prediction.jpg)

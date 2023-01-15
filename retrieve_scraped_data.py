import glassdoor_scrapper as gs
import pandas as pd

#This line will open a new chrome window and start the scraping.
path="C:/Users/ragha/Desktop/VIT/Projects/SalaryPrediction/chromedriver"
df = gs.get_jobs("data scientist", 3908, False, path)
#print(df)

#Make a csv file with the scraped data
df.to_csv("Salary_Prediction.csv", index = False)
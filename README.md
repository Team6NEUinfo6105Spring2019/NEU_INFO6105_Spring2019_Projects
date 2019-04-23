# NEU INFO6105 Spring2019 Team6 Projects
This repository contains the total 5 projects of Team6 in this semester, including 4 assignments and 1 final project. Please view the summary below and look through the details in sub-folders.

## Team Members
Zigeng Fu, Hao Cui, Yimu Jin, Ziyan Zhu

## Assignment1: Fintech Hiring Trends Analysis (Part 1)
### Summary
We analyzed 4 fintech reports of World Economic Forum (WEF), and totally 3,584 posted jobs on the careers site of 2 of the top U.S. banks, which are BNY Mellon and Capital One, and then figured out the insight on:
- Key fintech areas
- Job demands distributions
- Key fintech hiring trends
- Core competitiveness in fintech

### Tools and Methods
- Web scraping: Beautiful Soup
- Text extraction: pdfminer
- Keywords extraction: Word Count, TF-IDF, TextRank

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1-Tb8qcxYM2QH2U6BrbRFy_HdPpH1WVHb7nkiC8gkwTc#0


## Assignment2: Fintech Hiring Trends Analysis (Part 2)
### Summary
This project continue to analyze fintech hiring trends in banking industry with data from top 24 U.S. banks to come out scientific findings and predictions. The insight we gained on included:
- Fintech job contribution in 24 banks
- Fintech related job hiring trends
- Number and proportion of fintech related jobs in each of 24 banks
- Fitech categories with most jobs and least jobs
- Recommendations for job seekers in fintech area

### Tools and Methods
- Exploratory Data Analysis (EDA)
- Feature Engineering: clustering
- Docker
- Pipelining: Luigi, Airflow, Dask

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1mI2ATyKHXyLkZwq-8-KVx3s24uA8C9gKtrzXx98cZUk#0
- Video Presentation: https://www.youtube.com/watch?v=dpe_9bZGBM4


## Assignment3: Lending Club Loan Interest Rate Prediction
### Summary
Lending Club is a peer to peer lending company based in the United States, in which investors provide funds for potential borrowers and investors earn a profit depending on the risk they take (the borrowers credit score).
And arbitragers are people on Lending Club platform who can take advantage of their credit, borrow money at low interest rate, and then lend it out at high interest rate to make profit.
In this project, we decided to build machine learning models and select one with best performances to predict loan interst rate for arbitragers.

### Tools and Methods
- Machine Learning Models: NN, LR
- Manual vs Automated Feature Engineering
- AutoML: H2O, TPOT, Auto-SKLearn

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1mwss-8xq9ji4nPS8sN9bZD1rjvXWkbm59-eMQyppT7w#0
- Video Presentation: https://www.youtube.com/watch?v=39uDsF4bOiY&t=0s


## Assignment4: Music Mood Classification (Happy/Sad)
### Summary
In this project, we designed and developed a Chinese music mood classification App. Using this App, people can input Chinese lyrics and then predict the mood of the song (which is happy or sad) and the probability of the prediction.

### Tools and Methods
- Segment Analysis: Text Classification
- Neural Network: MLP
- Google Translate Api
- Web App DevOps: FLASK framework, heroku platform

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1UQlHwWT_0uEmYVj_D7ulWvFiVdK0-y1GbDgq1oufzsM#0
- Web App Demo: https://flask-info6105-music-app.herokuapp.com/
- Video Presentation: https://www.youtube.com/watch?v=oMeLmwlSaxA&t=0s


## Final Project: LoL Game Result Prediction
### Summary
LoL is the abbreviation of “League of Legends”, which is one of the most popular games in the world. In recent years, LoL has become an e-sport, and the seasonal championships are attracting more and more attention.
In this project, we will build a prediction model using MLP (Multi-Layer Perceptron), and use the datasets scraped from a Chinese game platform (https://www.wanplus.com/lol/) to train and test the machine learning model. Our goal is to predict the game result and its probability between a selected Chinese team and another team consists of 5 players. We will also develop a web application and deploy it online.

### Tools and Methods
- Data scraping: Beautiful Soup
- Data processing and EDA
- Model building: Neural Network (MLP)
- Model evaluation: MAPE, confusion matrix
- Hyper-parameter tuning
- Model comparison and selection: AutoML
- Web App DevOps: FLASK framework, heroku platform

### Links
To be determined...

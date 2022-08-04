# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:38:32 2022

@author: Alexander Hillert, Goethe University Frankfurt
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV


# adjust the directory to your folder
directory="C:/Lehre/Machine Learning/Data/"


# import the data for this problem
# NOTE: IT MIGHT TAKE 3 TO 5 MINUTES TO OPEN THE DATA
data_frame=pd.read_csv(directory+"form_10-Ks_machine_learning_2007_2008_all_variables_v1.csv",sep=";")
# The rows of the data are the Form 10-K filings. Each line is one filing.
# The columns are the variables. After some identifying information,
# you find the word frequencies, i.e., how often a word (e.g., "the") shows up
# in a 10-K (e.g., 100 times)


# WARNING: THE DATA SET IS TOO LARGE TO BE DISPLAYED -> Variable Explorer
# and Console will crash.
# However, you can pick a small subset of the data and look at it.
# It list all columns=variables and the first three observations.
data_frame_example=data_frame.head(3)
# you can click on this variable in the variable explorer without Spyder crashing.

# To see the variables included in the data use the following command
data_frame_column_names=data_frame.columns 
# you can click on this variable in the variable explorer without Spyder crashing.
# This variables shows all column/variable names in a vector.

# split the data set into the training and testing data
# we use the filings from year 2007 as training data
data_frame_train=data_frame[data_frame.year==2007]
# and the filing from year 2008 as testing data
data_frame_test=data_frame[data_frame.year==2008]

# put the cumulative abnormal return around the filing date into a new variable.
# we follow Loughran and McDonald (2011) and use the CAR from t to t+4.
# training data
filing_car_train=data_frame_train["excess_ret_t0_t4"]
# testing data
filing_car_test=data_frame_test["excess_ret_t0_t4"]

# so far, you have absolute word counts. For example, "loss" is found 5 times.
# As the length of the 10-Ks can be different, we scale by the number of words
# in the 10-K.
document_length_train=data_frame_train["number_of_words"]
document_length_test=data_frame_test["number_of_words"]


# the word frequencies are our independent variables -> restrict the data frame
# to those variables and drop all variables that are not needed
data_frame_train=data_frame_train.drop(columns=["cik","year","month","link","filing_type","filing_date","excess_ret_t0_t4","number_of_words"])
data_frame_test=data_frame_test.drop(columns=["cik","year","month","link","filing_type","filing_date","excess_ret_t0_t4","number_of_words"])

# compute relative frequencies, i.e., divide the absolute word count by document length
data_frame_train=data_frame_train.div(document_length_train, axis=0)
data_frame_test=data_frame_test.div(document_length_test, axis=0)

# standardize the data frames
# training data
data_frame_train_mean=np.mean(data_frame_train,axis=0)
data_frame_train_sd=np.std(data_frame_train, axis=0, ddof=1)
data_frame_train_standardized=(data_frame_train-data_frame_train_mean)/data_frame_train_sd
# testing data
data_frame_test_mean=np.mean(data_frame_test,axis=0)
data_frame_test_sd=np.std(data_frame_test, axis=0, ddof=1)
data_frame_test_standardized=(data_frame_test-data_frame_test_mean)/data_frame_test_sd


# There can be missing values in the standardized variables.
# They arise if the word count for a specific word is always zero in the training
# or in the testing data. In this case, the standard deviation is zero ->
# division by zero -> NaN.
# We replace these missing values by zero.
# training data
data_frame_train_standardized=data_frame_train_standardized.fillna(0)
# testing data
data_frame_test_standardized=data_frame_test_standardized.fillna(0)

##########################
# Ridge regression
##########################
print("\nRidge regression - Using cross-validation\n")
# Regress the CARs on the word frequencies using Ridge regressions with cross-validation.
# In this regression, we use the training data.
# We use five-fold cross-validation.
# Recommendation for initial alphas/lambdas: 100000, 150000, and 200000
# The optimal alpha is at around 140000.
regression_Ridge_cv=RidgeCV(alphas=[135000,137000,140000,143000,145000], fit_intercept=True,cv=5).fit(data_frame_train_standardized,filing_car_train)

# get the optimal lambda
alpha_optimal_cv=regression_Ridge_cv.alpha_
print("The optimal alpha is "+str(alpha_optimal_cv))

# what is the R2 in the training and testing data?
print("The R2 in the training data is: "+str(regression_Ridge_cv.score(data_frame_train_standardized,filing_car_train)))
print("The R2 in the testing data is: "+str(regression_Ridge_cv.score(data_frame_test_standardized,filing_car_test)))

# Mean squared error using the cross-validated model
# predict y in the full training sample
filing_car_train_predicted_Ridge=regression_Ridge_cv.predict(data_frame_train_standardized)
# predict y in the testing sample
filing_car_test_predicted_Ridge=regression_Ridge_cv.predict(data_frame_test_standardized)
# Determine the MSE
print("The MSE in the full training data is: "+str(mean_squared_error(filing_car_train, filing_car_train_predicted_Ridge)))
print("The MSE in the testing data is: "+str(mean_squared_error(filing_car_test, filing_car_test_predicted_Ridge)))


######################
# LASSO regression
######################
print("\nLASSO regression - Using cross-validation\n")
# Regress the CARs on the word frequencies using LASSO regressions with cross-validation.
# In this regression, we use the training data.
# We use five-fold cross-validation.
# Recommendation for initial alphas/lambdas: 0.5, 1, and 1.5
# The optimal alpha is at around 0.86.
regression_Lasso_cv=LassoCV(alphas=[0.85,0.86,0.87,0.88,0.89], fit_intercept=True,cv=5).fit(data_frame_train_standardized,filing_car_train)

# get the optimal lambda
alpha_optimal_cv=regression_Lasso_cv.alpha_
print("The optimal alpha is "+str(alpha_optimal_cv))

# get the R2 in the training data
print("The R2 in the training data is: "+str(regression_Lasso_cv.score(data_frame_train_standardized,filing_car_train)))
# ... and testing data
print("The R2 in the testing data is: "+str(regression_Lasso_cv.score(data_frame_test_standardized,filing_car_test)))

# Mean squared error using the cross-validated model
# predict y in the full training sample
filing_car_train_predicted_Lasso=regression_Lasso_cv.predict(data_frame_train_standardized)
# predict y in the testing sample
filing_car_test_predicted_Lasso=regression_Lasso_cv.predict(data_frame_test_standardized)
# Determine the MSE
print("The MSE in the full training data is: "+str(mean_squared_error(filing_car_train, filing_car_train_predicted_Lasso)))
print("The MSE in the testing data is: "+str(mean_squared_error(filing_car_test, filing_car_test_predicted_Lasso)))


############################################################
# Compare the betas from the Ridge and the LASSO regressions
############################################################
output_file=open(directory+"comparison_coefficients_Ridge_LASSO_10-Ks.csv","w",encoding="utf-8")
output_file.write("index;word;coefficient_Ridge;coefficient_LASSO\n")

# get the list of coefficients
for i in range (0,len(data_frame_train.columns)):
    output_file.write(str(i)+';'+data_frame_train.columns[i]+';'+str(regression_Ridge_cv.coef_[i])+';'+str(regression_Lasso_cv.coef_[i])+'\n')
    
output_file.close()

print("Completed!")

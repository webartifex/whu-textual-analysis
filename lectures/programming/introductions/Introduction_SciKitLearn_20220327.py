# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:38:32 2022

@author: Alexander Hillert, Goethe University Frankfurt
"""

'''
This script introduces you to linear models using the sklearn package.
Besides sklearn, we will use pandas to work with data sets as well as
numpy to perform computations.

The introduction consists of 10 parts:
1. linear regressions using a toy data set
2. linear regressions using a "real" data set
3. linear regressions using standardized variables
4. Ridge regression basics
5. Ridge regression with training, tuning, and testing sample
6. Ridge regression with cross-validation
7. LASSO regression basics
8. LASSO regression with training, tuning, and testing sample
9. LASSO regression with cross-validation
10. Compare the results from Ridge and LASSO

'''

import pandas as pd
import numpy as np
# For OLS regressions
from sklearn.linear_model import LinearRegression
# for Ridge regressions
from sklearn.linear_model import Ridge
# for computing mean squared errors
from sklearn.metrics import mean_squared_error
# for plotting the MSEs for different levels of Lambda
import matplotlib.pyplot as plot
# for Ridge regressions with cross-validation
from sklearn.linear_model import RidgeCV
# for LASSO regressions
from sklearn.linear_model import Lasso
# for LASSO regressions with cross-validation
from sklearn.linear_model import LassoCV

# adjust the directory to your folder!!!
directory="C:/Lehre/Machine Learning/Data/"

############################################################
# Part 1. Basics: linear regressions in Python using sklearn
############################################################
print("\nPart 1: Run an OLS regression on a sandbox data set\n")

# create a random number from a normal distribution with mean 0 and standard deviation 1.
random_number=np.random.normal(0, 1)
print("A random number is: "+str(random_number))

# you can also create a vector or matrix of random variables
# the parameter size(# of rows, # of columns) specifies the number rows and columns
# For example, a (10,1) vector
random_number_vector=np.random.normal(0, 1, size=(10,1))
print("The vector of random numbers is:")
print(random_number_vector)

# create the independent variable x as a vector of random numbers
x_vector=np.random.normal(0, 1, size=(10,1))
print("The vector of the independent variable x is:")
print(x_vector)

# create the dependent variable y as
# y = 2x + epsilon, where epsilon is the random error term from above
y_vector=np.dot(x_vector,2) + random_number_vector
print("The vector of the dependent variable y is:")
print(y_vector)

# perform a standard OLS regression with intercept.
# The command takes x (independent variable(s)) first and then y (dependent variable)
# Note that the default is that the intercept is included. So, strictly speaking,
# the (fit_intercept=True) option is not needed.
regression_1=LinearRegression(fit_intercept=True).fit(x_vector, y_vector)

# display the intercept and the beta coefficient on x
print("The intercept is: "+str(regression_1.intercept_))
# to get it as a scalar/number not an array, use
regression_1.intercept_[0]

print("The coefficient on x is: "+str(regression_1.coef_))
# to get it as a scalar/number not an array, use
regression_1.coef_[0][0]

# R2 of the regression
print("The R2 is: "+str(regression_1.score(x_vector, y_vector)))


###############################################################
# Part 2: linear regression using a "real" data set
###############################################################
print("\nPart 2: Run an OLS regression with a real data set\n")

# import the data for this problem
# The data set consists of 200 independent variables (x1 to x200) and
# a dependent variable (y).
# There are 1,200 observations in total. In the later parts, we will
# use the first 1,000 observations for training and the last 200 for testing.
# The data are simulated using the following process:
# y = 0.5*x1 + 0.5*x2 + ... + 0.5*x100 + random error (mean 0, std. dev. 4)
# The x101 to x200 are not directly related to y but are correlated with
# the x1 to x100. More specifically,
# x101 = 0.7*x1 + random error (mean 0, std. dev. 1)
# x102 = 0.7*x2 + random error (mean 0, std. dev. 1)
# x200 = 0.7*x100 + random error (mean 0, std. dev. 1)
data_frame=pd.read_csv(directory+"regression_data_scikit.csv",sep=";")

# to get any idea about the data, display the first five data points
data_frame.head(5)

# split the data frame into the independent and dependent variables
# the independent variables(x1 to x200) are columns 1 to 200
x_variables=data_frame.values[:,:-1]
# the dependent variable (y) is column 201
y_variable=data_frame.values[:,-1:]

# run a standard OLS regression
regression_OLS=LinearRegression(fit_intercept=True).fit(x_variables, y_variable)
# You can double check the results by reruning the regression in Stata or R.

# display the intercept and the beta coefficients on x1 and x51
print("The intercept is: "+str(regression_OLS.intercept_[0]))
print("The coefficient on x_1 is: "+str(regression_OLS.coef_[0][0]))
print("The coefficient on x_51 is: "+str(regression_OLS.coef_[0][50]))

# R2 of the regression
print("The R2 is: "+str(regression_OLS.score(x_variables, y_variable)))


##################################################################
# Part 3: standardize the data to have mean zero and unit variance
# and rerun the regression
##################################################################
print("\nPart 3a.: Standardize variables\n")

# standardize x and y to have mean zero and unit variance
# axis=0 (axis=1) means that the computation is executed column (row) wise
x_variables_mean=np.mean(x_variables,axis=0)
# ddof=1 means that we use n-1 to compute the standard deviation
x_variables_standard_deviation=np.std(x_variables, axis=0, ddof=1)
x_variables_standardized=(x_variables-x_variables_mean)/x_variables_standard_deviation 

# do the same exercise for y
y_variable_mean=np.mean(y_variable,axis=0)
y_variable_standard_deviation=np.std(y_variable, axis=0, ddof=1)
y_variable_standardized=(y_variable-y_variable_mean)/y_variable_standard_deviation 

# rerun the regression using standardized data
regression_OLS_standardized=LinearRegression(fit_intercept=True).fit(x_variables_standardized, y_variable_standardized)
# results are identical to a regression in Stata with beta coefficients.

# display the intercept and the beta coefficients on x_1 and x_51
print("The intercept is: "+str(regression_OLS_standardized.intercept_[0]))
print("The coefficient on x_1 is: "+str(regression_OLS_standardized.coef_[0][0]))
print("The coefficient on x_51 is: "+str(regression_OLS_standardized.coef_[0][50]))

# R2 of the regression
print("The R2 is: "+str(regression_OLS_standardized.score(x_variables_standardized, y_variable_standardized)))
# The R2 is identical to the one from Part 2 -> good!

#######################################################################################
# CAUTION: be careful using the "normalize=True" option in the LinearRegression module!
#######################################################################################
print("\nPart 3b.: Regression with 'normalization'\n")
# Normalizer works on the rows, not the columns!
# By default, L2 normalization is applied to each observation so that the
# values in a row (!) have a unit norm. Unit norm with L2 means that if each 
# element were squared and summed, the total would equal 1. 
regression_OLS_normalized=LinearRegression(fit_intercept=True,normalize=True).fit(x_variables, y_variable)

# display the intercept and the beta coefficient on x_1 and x_51
print("The intercept is: "+str(regression_OLS_normalized.intercept_[0]))
print("The coefficient on x_1 is: "+str(regression_OLS_normalized.coef_[0][0]))
print("The coefficient on x_51 is: "+str(regression_OLS_normalized.coef_[0][50]))
# The coefficients are different from the ones above highlighting that the
# "normalize=True" option does not do the same as "normal" standardizing
# R2 of the regression
print("The R2 is: "+str(regression_OLS_normalized.score(x_variables, y_variable)))


#######################################################################
# Part 4: Ridge regression on the full sample (no training and testing)
# This part is to learn the syntax.
# We are using the standardized variables to have the same penalty 
# for a given effect of x on y.
# Remember: if the independent variables are measured on very different
# scales, the beta coefficients have different sizes (e.g., market cap in 
# thousand USD vs. past stock returns as a decimal number) and, thus, 
# the panelty would be applied inconsistently.
#######################################################################
print("\nPart 4: Ridge regression - learning the syntax\n")

# the parameter alpha corresponds to the penalty parameter Lambda from
# the notation that is typically used.
# the default is that the intercept is included, so you do not need the
# "intercept=True" parameter. But it is good to keep in mind what
# specification you are using.
regression_Ridge=Ridge(alpha=10,fit_intercept=True).fit(x_variables_standardized, y_variable_standardized)

# display the intercept and the beta coefficient on x1 and x51
print("The intercept is: "+str(regression_Ridge.intercept_[0]))
print("The coefficient on x_1 is: "+str(regression_Ridge.coef_[0][0]))
print("The coefficient on x_51 is: "+str(regression_Ridge.coef_[0][50]))

# R2 of the regression
print("The R2 is: "+str(regression_Ridge.score(x_variables_standardized, y_variable_standardized)))

# How to compute the mean squared error (MSE)?
# 1. get the predicted values
y_variable_standardized_predicted=regression_Ridge.predict(x_variables_standardized)
# 2. determine the MSE
print("The MSE of the prediction is: "+str(mean_squared_error(y_variable_standardized, y_variable_standardized_predicted)))


#######################################################################
# Part 5: Ridge regression using a training, tuning, and testing sample
#######################################################################
print("\nPart 5: Ridge regression - Application with training, tuning, and testing data\n")

# Create a training, tuning, and testing sample
# we split the data into a training, a tuning, and a testing set
# training data are the frist 800 rows
# In the brackets, the first range (before the comma) indicates the rows, the second the columns.
x_variables_std_train=x_variables_standardized[:800,:]
y_variable_std_train=y_variable_standardized[:800,:]
# the tuning data are row 801 to 1000 -> 200 observations
x_variables_std_tune=x_variables_standardized[800:1000,:]
y_variable_std_tune=y_variable_standardized[800:1000,:]
# testing data are the last 200 rows
x_variables_std_test=x_variables_standardized[1000:,:]
y_variable_std_test=y_variable_standardized[1000:,:]


##########################
# find the optimal Lambda
##########################
# we store the MSE of the training/tuning data for each Lambda
mse_train_list=[]
mse_tune_list=[]
# Again, Lambda and Alpha refer to the same thing.
alpha_list=[]

# we iterate from 0.1 to 100 increasing Lambda=Alpha by 0.1 in each step.
alpha=0.1
while alpha<100:
    # train the model
    regression_Ridge_train=Ridge(alpha=alpha,fit_intercept=True).fit(x_variables_std_train, y_variable_std_train)
    # add the alpha to the list of alphas
    alpha_list.append(alpha)
    # predict y in the training sample
    y_variable_std_train_predicted=regression_Ridge_train.predict(x_variables_std_train)
    # predict y in the tuning sample
    y_variable_std_tune_predicted=regression_Ridge_train.predict(x_variables_std_tune)
    # compute the MSE in both samples
    mse_train=mean_squared_error(y_variable_std_train, y_variable_std_train_predicted)
    mse_tune=mean_squared_error(y_variable_std_tune, y_variable_std_tune_predicted)
    # append the MSEs to the two lists
    mse_train_list.append(mse_train)
    mse_tune_list.append(mse_tune)
    # continue with the next alpha
    alpha=alpha+0.1

########################################
# plot the MSEs for the different alphas
########################################
# MSE in the training sample
plot.scatter(alpha_list, mse_train_list)
plot.show()
# higher Lambda associated with higher MSE

# MSE in the tuning sample
plot.scatter(alpha_list, mse_tune_list)
plot.show()
# there is an optimal alpha with the lowest MSE

######################################
# determine the optimal Lambda
######################################
# what is the smallest MSE?
minimum=min(mse_tune_list)
print("The smallest MSE is "+ str(minimum))
# get the position of the minimum MSE in our list
index_min_MSE=mse_tune_list.index(minimum)
# choose the corresponding alpha
alpha_optimal=alpha_list[index_min_MSE]
print("The optimal alpha is "+str(alpha_optimal))

#############################################################
# What is the out-of-sample performance of the optimal model?
#############################################################
# take the full training data set (1000 observations, i.e., training + tuning set)
x_variables_std_train_total=np.concatenate((x_variables_std_train, x_variables_std_tune), axis=0)
y_variable_std_train_total=np.concatenate((y_variable_std_train, y_variable_std_tune), axis=0)
# train the model with the optimal Lambda on the training and tuning data
regression_Ridge_optimal=Ridge(alpha=alpha_optimal,fit_intercept=True).fit(x_variables_std_train_total, y_variable_std_train_total)

# Mean squared error
# predict y in the full training sample
y_variable_std_train_total_predicted=regression_Ridge_optimal.predict(x_variables_std_train_total)
# predict y in the testing sample
# Remeber: we have not used the testing data yet. Firewall principle!!!
y_variable_std_test_predicted=regression_Ridge_optimal.predict(x_variables_std_test)

print("The MSE in the full training data is: "+str(mean_squared_error(y_variable_std_train_total, y_variable_std_train_total_predicted)))
print("The MSE in the testing data is: "+str(mean_squared_error(y_variable_std_test, y_variable_std_test_predicted)))


#############################################################
# Part 6: Ridge regression with k-fold cross-validation 
# Implement the cross validation using a package
#############################################################
print("\nPart 6. Ridge regression - Using cross-validation\n")

# the default for cv is the leave-one-out cross-validation
# here we apply five-fold cross-validation
regression_Ridge_cv=RidgeCV(alphas=alpha_list, fit_intercept=True,cv=5).fit(x_variables_std_train_total,y_variable_std_train_total)

# get the optimal lambda
alpha_optimal_cv=regression_Ridge_cv.alpha_
print("The optimal alpha is "+str(alpha_optimal_cv))

# Mean squared error using the cross-validated model
# predict y in the full training sample
y_variable_std_train_total_predicted_cv=regression_Ridge_cv.predict(x_variables_std_train_total)
# predict y in the testing sample
y_variable_std_test_predicted_cv=regression_Ridge_cv.predict(x_variables_std_test)

print("The MSE in the full training data is: "+str(mean_squared_error(y_variable_std_train_total, y_variable_std_train_total_predicted_cv)))
print("The MSE in the testing data is: "+str(mean_squared_error(y_variable_std_test, y_variable_std_test_predicted_cv)))


###########################################
# Part 7: LASSO regression
# on the full sample -> to learn the syntax
###########################################

print("\nPart 7: LASSO regression - learning the syntax\n")
# the parameter alpha corresponds to the penalty parameter Lambda from
# the notation that is typically used.
# the default is that the intercept is included, so you do not need the
# "intercept=True" parameter. But it is good to keep in mind what
# specification you are using.
regression_Lasso=Lasso(alpha=0.1,fit_intercept=True).fit(x_variables_standardized, y_variable_standardized)

# display the intercept and the beta coefficient on x1 and x51
print("The intercept is: "+str(regression_Lasso.intercept_[0]))
print("The coefficient on x_1 is: "+str(regression_Lasso.coef_[0]))
print("The coefficient on x_51 is: "+str(regression_Lasso.coef_[50]))

# R2 of the regression
print("The R2 is: "+str(regression_Lasso.score(x_variables_standardized, y_variable_standardized)))

# How to compute the mean squared error (MSE)?
# 1. get the predicted values
y_variable_standardized_predicted=regression_Lasso.predict(x_variables_standardized)
# 2. determine the MSE
print("The MSE of the prediction is: "+str(mean_squared_error(y_variable_standardized, y_variable_standardized_predicted)))


####################################################
# Part 8: Create a training, tune and testing sample
####################################################
print("\nPart 8: LASSO regression - Application with training, tuning, and testing data\n")
# we use the same training, tuning, and testing data as in part 5.
# -> no need to redefine the data sets.

#################################
# find the optimal Lambda
#################################
# we store the MSE of the training/tuning data for each Lambda
mse_train_list=[]
mse_tune_list=[]
# Again, Lambda and Alpha refer to the same thing.
alpha_list=[]

# we iterate from 0.0001 to 0.25 increasing alpha by 0.0001 in each step.
alpha=0.0001
while alpha<0.25:
    # train the model
    regression_Lasso_train=Lasso(alpha=alpha,fit_intercept=True).fit(x_variables_std_train, y_variable_std_train)
    # add the alpha to the list of alphas
    alpha_list.append(alpha)
    # predict y in the training sample
    y_variable_std_train_predicted=regression_Lasso_train.predict(x_variables_std_train)
    # predict y in the tuning sample
    y_variable_std_tune_predicted=regression_Lasso_train.predict(x_variables_std_tune)
    # compute the MSE in both samples
    mse_train=mean_squared_error(y_variable_std_train, y_variable_std_train_predicted)
    mse_tune=mean_squared_error(y_variable_std_tune, y_variable_std_tune_predicted)
    # append the MSEs to the two lists
    mse_train_list.append(mse_train)
    mse_tune_list.append(mse_tune)
    # continue with the next alpha
    alpha=alpha+0.0001

########################################
# plot the MSEs for the different alphas
########################################

# MSE in the training sample
plot.scatter(alpha_list, mse_train_list)
plot.show()
# higher Lambda associated with higher MSE

# MSE in the tuning sample
plot.scatter(alpha_list, mse_tune_list)
plot.show()
# there is an optimal alpha with the lowest MSE


######################################
# determine the optimal Lambda
######################################
# what is the smallest MSE?
minimum=min(mse_tune_list)
print("The smallest MSE is "+ str(minimum))
# get the position of the minimum MSE
index_min_MSE=mse_tune_list.index(minimum)
alpha_optimal=alpha_list[index_min_MSE]

print("The optimal alpha is "+str(alpha_optimal))

#############################################################
# What is the out-of-sample performance of the optimal model?
#############################################################
# take the full training data set (1000 observations; training + tuning)
# use the same variables as in Part 5.

# train the model with the optimal Lambda on the training and tuning data
regression_Lasso_optimal=Lasso(alpha=alpha_optimal,fit_intercept=True).fit(x_variables_std_train_total, y_variable_std_train_total)

# Mean squared error
# predict y in the full training sample
y_variable_std_train_total_predicted=regression_Lasso_optimal.predict(x_variables_std_train_total)
# predict y in the testing sample
y_variable_std_test_predicted=regression_Lasso_optimal.predict(x_variables_std_test)

print("The MSE in the full training data is: "+str(mean_squared_error(y_variable_std_train_total, y_variable_std_train_total_predicted)))
print("The MSE in the testing data is: "+str(mean_squared_error(y_variable_std_test, y_variable_std_test_predicted)))


#############################################################
# Part 9: Implement the cross validation using a package
#############################################################
print("\nPart 9: LASSO regression - Using cross-validation\n")

# the default for cv in LassoCV is the 5-fold cross-validation
regression_Lasso_cv=LassoCV(alphas=alpha_list, fit_intercept=True,cv=5).fit(x_variables_std_train_total,y_variable_std_train_total)

# get the optimal lambda
alpha_optimal_cv=regression_Lasso_cv.alpha_
print("The optimal alpha is "+str(alpha_optimal_cv))

# Mean squared error using the cross-validated model
# predict y in the full training sample
y_variable_std_train_total_predicted_cv=regression_Lasso_cv.predict(x_variables_std_train_total)
# predict y in the testing sample
y_variable_std_test_predicted_cv=regression_Lasso_cv.predict(x_variables_std_test)

print("The MSE in the full training data is: "+str(mean_squared_error(y_variable_std_train_total, y_variable_std_train_total_predicted_cv)))
print("The MSE in the testing data is: "+str(mean_squared_error(y_variable_std_test, y_variable_std_test_predicted_cv)))


#####################################################################
# Part 10: Compare the betas from the Ridge and the LASSO regressions
#####################################################################
print("\nPart 10: Comparison of Ridge and LASSO coefficients\n")
# To set to what extend the results of Ridge and LASSO are similar, we
# write the coefficients from the cross-validation tasks (Parts 6 and 9)
# to a csv files.

output_file=open(directory+"comparison_coefficients_Ridge_LASSO.csv","w",encoding="utf-8")
output_file.write("index;coefficient_Ridge;coefficient_LASSO\n")

# get the list of coefficients
for i in range (0,200):
    output_file.write(str(i)+';'+str(regression_Ridge_cv.coef_[0][i])+';'+str(regression_Lasso_cv.coef_[i])+'\n')
    
output_file.close()

print("Completed!")

# Project Summary
*Predict the price of homes at sale for the Ames Iowa Housing dataset.* 

Based on [House Prices: Advanced Regression Techniques Kaggle Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

# Contents:
- [Problem Statement](#Problem-Statement)
- [Executive Summary](#Executive-Summary)
- [Data Summary](#Data-Summary)
- [Models and Techniques](#Models-and-Techniques)
- [Conclusions](#Conclusions)

# Problem Statement
Create a regression model based on the Ames Housing Dataset that predicts the price of a house at sale.

# Executive Summary
In this project we were tasked with creating a regression model based on the Ames Housing Dataset that predicts the price of a house at sale. The approach, as represented in the respective notebooks, was split into two phases: Exploratory Data Analysis (EDA) and Modeling. Our models were then tested on unseen data, scored, and ranked relative to the models of other members of our cohort.  

I submitted a total of 13 models, 4 of which are included in my Models workbook. Each model improves sequentially, illustrating my process.

At a high level, there are two clear themes when it comes to fitting a good multiple linear regression model, based on my models. First, taking the log of y, SalePrice, increases the model’s performance by all measures used. We saw this between Model 1 and Model 2. Second, increasing the number of dependent variables is generally a good thing. We observed this between Model 0 to Model 1 as well as Model 2 to Model 3. In the case of the latter, the increase was substantial (from 16 features to 303 features). Certainly, this leaves plenty of room for further investigation and fine tuning.

# Data Summary
**Data Source:**
- The data for this project came from General Assembly’s [DSI-US-11 Project 2 Regression Challenge](https://www.kaggle.com/c/dsi-us-11-project-2-regression-challenge), which is an adapted version of the data in [Kaggle's Ames Housing Data competition](https://www.kaggle.com/c/ames-housing-data).
- In all datasets, each row represents a home and each column a various feature used in computing assessed home values.

**Datasets:**
- [train.csv](./datasets/train.csv)
  -  Original training data set (2501 rows, 81 columns)
- [test.csv](./datasets/test.csv])
  - Original testing data set, same columns as train.csv excluding target variable  SalePrice (878 rows, 80 columns)
- [train_processed.csv](./datasets/train_processed.csv)
  - Reflects changes to train.csv, most notably dropping outliers and adding dummy columns for categorical features (2049 rows, 304 columns)
- [test_processed.csv](./datasets/test_processed.csv)
  -   Includes same changes to features as train_processed.csv (878 rows, 286 columns)


No outside datasets were used.
### Data Dictionary
Features listed in the data dictionary below represent those features included in the model I submitted to Kaggle. A full list of feature descriptions can be found [here](./data_description.txt).


|Feature|Type|Dataset|Description|
|--|--|--|--|
|**Overall Qual**|*ordinal*|train|Rates the overall material and finish of the house (1-10 with 1 being Very Poor and 10 Very Excellent)|
|**Garage Area**|*float*|train|Size of garage in square feet|
|**1st Flr SF**|*float*|train|First Floor square feet|
|**MS SubClass**|*nominal*|train|Identifies the type of dwelling involved in the sale (16 categories)|
|**Lot Frontage**|*float*|train|Linear feet of street connected to property|
|**Year Built**|*int*|train|Original construction date|
|**Year Remod/Add**|*int*|train|Remodel date (same as construction date if no remodeling or additions)|
|**Full Bath**|*int*|train|Number of full bathrooms above ground|
|**TotRms AbvGrd**|*int*|train|Total rooms above ground (does not include bathrooms)|
|**Fireplaces**|*int*|train|Number of fireplaces|
|**Heating QC_Ex**|*ordinal*|train|Heating quality and condition (5-point scale from Poor to Excellent)|
|**Neighborhood_NridgHt**|*int*|train_processed|dummy of 'Neighborhood' for Northridge Heights neighborhood|
|**Exter Qual_TA**|*int*|train_processed|dummy of 'Exter Qual', which evaluates the quality of the material on the exterior; TA for Average/Typical |
|**Open Porch SF**|*float*|train|Open porch area in square feet|
|**Wood Deck SF**|*float*|train|Wood deck area in square feet|
|**Central Air_Y**|*int*|train_processed|has central air conditioning|

# Models and Techniques
- Our predictions are based on a multiple linear regression (MLR) model. The dependent variables used in the final model are a combination of features included in the original dataset as well as dummies from some of the categorical features.
- The 02_Models notebook contains 3 models, excluding the model used to calculate the baseline score, with each progressive model improving.
- Model 0 took in the top 2 correlated variables and was used to calculate the baseline score. Model 1 is composed of 16 prediction features, taken from the top 15 positively and negatively correlated features. Model 2, the model used in the Kaggle submission, is the same as Model 1, except it is fit using log y. Finally, Model 3 takes in all numeric variables (including dummies).
- Evaluation metrics were root mean squared error (RMSE), mean absolute error (MAE), as well as R2 scores for each train, test, and cross validation.

# Conclusions
- At a high level, there are two clear themes when it comes to fitting a good MLR model, based on my models. First, taking the log of y, SalePrice, increases the model’s performance by all measures used. We saw this between Model 1 and Model 2. Second, increasing the number of dependent variables is generally a good thing. We observed this between Model 0 to Model 1 as well as Model 2 to Model 3. In the case of the latter, the increase was substantial (from 16 features to 303 features). Certainly, this leaves plenty of room for further investigation and fine tuning.
- The features included in Models 2&3 illustrate that it can be important to include both positively and negatively correlated variables. This is can be counterintuitive, in that people generally associate positively correlated features to predicting a target y. However, when we get our coefficients on well-chosen negatively correlated features, this can help to decrease residuals.

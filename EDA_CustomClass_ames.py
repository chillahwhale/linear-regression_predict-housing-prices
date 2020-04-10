#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# see EDA_Blank.py file in week 3 EDA_workflow folder
# ref video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM

## IDEAS for what to add:
# sns.lmplot(x='', y='', data=df, ci=False, fit_reg=False);
## fits linear regression model over scatterplot
## fit_reg puts line of best fit over top


## example of how to call this:
## my filename is called EDA_Class.py
## my class within that file is called CleanData
## we import this the same way we import a library
# from EDA_Class import CleanData
# # in order to use your class, you have to create an instance of it
# # clean is an instance of CleanData
# clean = CleanData(college)
# # missing_values checks
# clean.missing_values()

class CleanExplore:
# class adapted from Noelle Brown and further developed by Matt Burke
    import numpy as np
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy.stats as stats
    import matplotlib.pyplot as plt
    from sklearn import metrics
    from sklearn.linear_model import LinearRegression

    def __init__(self, df):
# init() method allows us to not call dataframe on other methods
        self.df = df

    def snapshot(self):
# print basic info about dataframe
        print(f'\nSHAPE \n{self.df.shape} \n \nCOLUMNS \n{self.df.columns} \n \nDTYPES \n{self.df.dtypes}\n \nUNIQUES \n{self.df.nunique()} \n \nINFO \n{self.df.info()} \n \nINFO \n{self.df.info()} \n \nDESCRIPTION \n{self.df.describe().round()}\n \nNULL VALUES \n{self.df.isnull().sum()} \n')

    def drop_missing(self):
# drop all rows with missing values
# credit: Noelle Brown
        return self.df.dropna()

    def chart_corr_diag(self):
# plot diaganol correlation chart
# source: https://seaborn.pydata.org/examples/many_pairwise_correlations.html

        # Compute the correlation matrix
        corr = self.df.corr()
        # Generate a mask for the upper triangle
        mask = self.np.triu(self.np.ones_like(corr, dtype=self.np.bool))
        # Set up the matplotlib figure
        f, ax = self.plt.subplots(figsize=(11, 9))
        # Generate a custom diverging colormap
        cmap = self.sns.diverging_palette(220, 10, as_cmap=True)
        # Draw the heatmap with the mask and correct aspect ratio
        self.sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1, center=0,
                    square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .5});

    def print_null_objects(self):
# print value counts for all 'objects' with more than 1 null value
# source: https://medium.com/@hjhuney/quantitative-data-exploration-for-regression-in-python-ames-housing-part-1-25879dd4cc4a
        for i in self.df:
            if self.df[i].dtype == object :
                if self.df[i].isnull().sum() > 0:
                    print(self.df[i].value_counts())
                    print("Number of Null Values: " + str(self.df[i].isnull().sum()))
                    print("Percentage of Nulls = " + str(self.np.round((self.df[i].isnull().sum() / 14.60), 2)) + "%")
                    print("\n")

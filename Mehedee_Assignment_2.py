#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:44:34 2023

Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com


Problem: Please write a Python script for investigating whether there is a statistical relation between
         the two data series and plot the data and a regression line.
                
Data sources:
        - https://fred.stlouisfed.org/series/QDER368BIS (Germany)
        - https://fred.stlouisfed.org/series/QATR368BIS (Austria)


"""

""" Module imports"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

""" Function definitions"""
def main():
    
    """ 1. Load data"""
    df_Ger = pd.read_csv("QDER368BIS.csv")
    df_Aus = pd.read_csv("QATR368BIS.csv")
    
    print(df_Ger)
    print(df_Aus)
    
    """ 2. Clean data frames"""
    """ Transform data format of DATE column"""
    df_Ger["DATE"] = pd.to_datetime(df_Ger["DATE"])
    df_Aus["DATE"] = pd.to_datetime(df_Aus["DATE"])
    
    """ Assign readable column names"""
    df_Ger.columns = ["Date", "Rate_of_Property_Germany"]
    df_Aus.columns = ["Date", "Rate_of_Property_Austria"]
    
    print(df_Ger)
    print(df_Aus)

    """ 3. Merge data frames"""
    df = pd.merge(df_Ger, df_Aus, on="Date", how="inner")
    print("/nMerge data/n/n",df)
    
    """ 4. Plot the data"""
    fig, ax = plt.subplots(nrows=2, ncols=1, squeeze=False)
    ax[0][0].plot(df["Date"], df["Rate_of_Property_Germany"], color="b")
    """ Plot black line at 0"""
    ax[0][0].plot(df["Date"], df["Rate_of_Property_Germany"] * 0, color="k")
    ax[0][0].fill_between(df["Date"], df["Rate_of_Property_Germany"] * 0, 
                                      df["Rate_of_Property_Germany"], color="b", alpha=0.25)
    ax[0][0].set_xlabel("Date")
    ax[0][0].set_ylabel("Rate of Property in Germany")
    ax[1][0].plot(df["Date"], df["Rate_of_Property_Austria"], color="g")
    """ Plot black line at 0"""
    ax[1][0].plot(df["Date"], df["Rate_of_Property_Austria"] * 0, color="k")
    ax[1][0].fill_between(df["Date"], df["Rate_of_Property_Austria"] * 0, 
                                      df["Rate_of_Property_Austria"], color="g", alpha=0.25)
    ax[1][0].set_xlabel("Date")
    ax[1][0].set_ylabel("Rate of Property in Austria")
    plt.tight_layout()
    plt.show()
    
    """5. Perform regression"""
    linear_model = smf.ols(formula="Rate_of_Property_Austria ~ Rate_of_Property_Germany", data=df)
    linear_model_fit = linear_model.fit()
    print(linear_model_fit.params)
    print(linear_model_fit.summary())
    df["Regression"] = linear_model_fit.predict()
    
    """ 6. Plot data and regression line"""
    fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
    ax[0][0].scatter(df["Rate_of_Property_Germany"], df["Rate_of_Property_Austria"], color="b", s=5)
    ax[0][0].plot(df["Rate_of_Property_Germany"], df["Regression"], color="r")
    ax[0][0].set_xlabel("Rate of Property in Germany")
    ax[0][0].set_ylabel("Rate of Property in Austria")
    plt.tight_layout()
    plt.show()
    
    """ The plot (data and regression line) can also be plotted with
            statsmodels.api.graphics.plot_ccpr()"""
    fig = sm.graphics.plot_ccpr(linear_model_fit, "Rate_of_Property_Germany")
    fig.tight_layout()
    fig.show()
    
    """ Other plots from statsmodels.api provide other information about the 
    data and fit, e.g., """
    # Fit and confidence compared to data
    fig = sm.graphics.plot_fit(linear_model_fit, "Rate_of_Property_Germany")
    fig.tight_layout()
    fig.show()

    # Influence by observation
    fig = sm.graphics.influence_plot(linear_model_fit, criterion="cooks")
    fig.tight_layout()
    fig.show()
    
    # Residuals (QQ-plot)
    fig = sm.qqplot(linear_model_fit.resid, line="s")
    fig.tight_layout()
    fig.show()
        
    
""" Class definitions"""

""" Main entry point"""
if __name__ == '__main__':
    main()
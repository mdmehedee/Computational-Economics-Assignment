#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 23:40:10 2023

Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com


Problem: Please choose one country for which you can find the required data for Y , K, and L (e.g.,
         from the Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/) and write
         a Python script for loading and merging the data and performing the regression. Hint: As
         you know, you can compute the logarithm of a pandas data series with numpy.log, e.g.
         df["log\_GDP"] = np.log(df["GDP"]).
                
Data sources:
        - https://fred.stlouisfed.org/series/MKTGDPDEA646NWDB (GDP, Germany)
        - https://fred.stlouisfed.org/series/CKSPPPDEA666NRUG (Capital stock, Germany)
        - https://fred.stlouisfed.org/series/POPTOTDEA647NWDB (Population, Germany)

"""

""" Module imports"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as smstats
""" Function definitions"""
def main():
    
    """ 1. Load data"""
    df_GDP = pd.read_csv("MKTGDPDEA646NWDB.csv")
    df_CS = pd.read_csv("CKSPPPDEA666NRUG.csv")
    df_POP = pd.read_csv("POPTOTDEA647NWDB.csv")
    
    print(df_GDP)
    print(df_CS)
    print(df_POP)
    
    """ 2. Clean data frames"""
    """ Transform data format of DATE column"""
    df_GDP["DATE"] = pd.to_datetime(df_GDP["DATE"])
    df_CS["DATE"] = pd.to_datetime(df_CS["DATE"])
    df_POP["DATE"] = pd.to_datetime(df_POP["DATE"])
    
    
    """ 3. Assign readable column names"""
    df_GDP.columns = ["Date", "GDP"]
    df_CS.columns = ["Date", "Capital_stock"]
    df_POP.columns = ["Date", "Population"]
    
    df_CS["Capital_stock"] = df_CS["Capital_stock"] * 1000000
    print("GDP:", df_GDP)
    print("Capital_stock:", df_CS)
    print("Population:", df_POP)

    """ 4. Merge data frames"""
    df_GDP_CS = pd.merge(df_GDP, df_CS, on="Date", how="inner")
    df_GDP_CS_POP = pd.merge(df_GDP_CS, df_POP, on="Date", how="inner")
    print("Merged data:",df_GDP_CS_POP)
    
    
    
    """ 5. Compute the logarithm of a pandas data series"""
    df_GDP_CS_POP["GDP"] = np.log(df_GDP_CS_POP["GDP"])
    df_GDP_CS_POP["Capital_stock"] = np.log(df_GDP_CS_POP["Capital_stock"])
    df_GDP_CS_POP["Population"] = np.log(df_GDP_CS_POP["Population"])
    df = pd.concat([df_GDP_CS_POP["GDP"], df_GDP_CS_POP["Capital_stock"], df_GDP_CS_POP["Population"]], keys=['Y', 'K', 'L'], axis=1)
    
    """6. Perform regression"""
    linear_model = smf.ols(formula="Y ~ K + L", data=df)
    linear_model_fit = linear_model.fit()
    print(linear_model_fit.params)
    print(linear_model_fit.summary())
    
    pb_test = smstats.het_breuschpagan(linear_model_fit.resid, linear_model_fit.model.exog)
    print("Breuschpagan Test:", pb_test)
    df["Regression"] = linear_model_fit.predict()
    
    
""" Class definitions"""

""" Main entry point"""
if __name__ == '__main__':
    main()
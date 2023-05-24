import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

def plotMeanDailySunDuration(meanSunDuration, minYear, maxYear, location):
    """Plots the mean daily sun duration and adds descriptions. Timespan description specified by min and maxYear, Location by location.

    Args:
        meanSunDuration (list like): list of daily sun durations
        minYear (numerical): lower bound of time data used
        maxYear (numerical): upper bound of time data used
        location (numerical): location of data acquisition
    """
    plt.grid(which='both', axis='y')
    plt.bar(range(1,367), meanSunDuration)
    plt.title(f'Zeitraum: {minYear} - {maxYear}, Ort: {location}')
    plt.suptitle('Mittlere tägliche Sonnenscheindauer')
    plt.ylabel('Sonnenscheindauer pro Tag [h]')
    plt.xlabel('Tag im Jahr')
    plt.show()

def calcMeanDailySunDuration(df):
    """Generates mean daily value dataframe from raw hourly data over multiple years

    Args:
        df (pandas Dataframe): Dataframe containing raw data. Must contain column 'Zeitstempel' for time data and 'Wert' for value to be averaged

    Returns:
        pandas Dataframe: mean daily value 
    """
    df['TimeStamp'] = pd.to_datetime(df['Zeitstempel'])

    df.drop('Zeitstempel', axis=1, inplace=True)

    df['Year'] = df['TimeStamp'].dt.year
    df['DayOfYear'] = df['TimeStamp'].dt.day_of_year
    df['Hour'] = df['TimeStamp'].dt.hour

    return df.groupby(['DayOfYear'])['Wert'].mean()


sunDurationDf = pd.read_csv(r"C:\Users\lelem\Projekte\WetterDatenanalyse\WeatherDataAnalysisESS\Data\cdc_download_2023-05-17_14-28\data\data_OBS_DEU_PT1H_SD.csv", index_col=False)

meanSunDuration = calcMeanDailySunDuration(df=sunDurationDf)

minYear = sunDurationDf['Year'].min()
maxYear = sunDurationDf['Year'].max()
location = 'Essen Bredeney'
plotMeanDailySunDuration(meanSunDuration, minYear, maxYear, location)
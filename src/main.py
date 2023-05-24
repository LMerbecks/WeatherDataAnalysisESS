import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

def plotMeanDaily(meanDailyValue, datatitle, ylabel, minYear, maxYear, location):
    """Plots the mean daily sun duration and adds descriptions. Timespan description specified by min and maxYear, Location by location.

    Args:
        meanDailyValue (list like): list of mean daily values
        datatitle (string): title of data type e.g. sun duration
        ylabel (string): label for y axis (should be similar to datatitle)
        minYear (numerical): start year of data acquisition
        maxYear (numerical): last year of data acquisition
        location (string): locaiton of data acquisition
    """
    fig = plt.figure()
    plt.grid(which='both', axis='y')
    plt.bar(range(1,367), meanDailyValue)
    plt.title(f'Zeitraum: {minYear} - {maxYear}, Ort: {location}')
    plt.suptitle(datatitle)
    plt.ylabel(ylabel)
    plt.xlabel('Tag im Jahr')
    fig.show()

def plotMeanHourly(meanHourlyValue, datatitle, ylabel, yearLimits, location):
    """Plots mean value for all hours of a day

    Args:
        meanHourlyValue (list): list of mean hourly values
        datatitle (string): title of data type e.g. sun duration
        ylabel (string): label for y axis (should be similar to datatitle)
        yearLimits (list): list with first and last year of data acquisition
        location (string): locaiton of data acquisition
    """
    fig = plt.figure()
    plt.grid(which='both', axis='y')
    plt.bar(range(0,24), meanHourlyValue)
    plt.title(f'Zeitraum: {yearLimits[0]} - {yearLimits[1]}, Ort: {location}')
    plt.suptitle(datatitle)
    plt.ylabel(ylabel)
    plt.xlabel('Stunde am Tag')
    fig.show()





def calcMeanDaily(df, valueColumn):
    """Generates mean daily value dataframe from raw hourly data over multiple years

    Args:
        df (pandas Dataframe): Dataframe containing raw data. Must contain column 'Zeitstempel' for time data and 'Wert' for value to be averaged
        valueColumn (string): column identifier of column containing data to be averaged

    Returns:
        pandas Dataframe: mean daily value 
    """

    df['Year'] = df['TimeStamp'].dt.year
    df['DayOfYear'] = df['TimeStamp'].dt.day_of_year
    df['Hour'] = df['TimeStamp'].dt.hour

    return df.groupby(['DayOfYear'])[valueColumn].mean()


def calcMeanHourly(df, valueColumn):
    """Calculates hourly mean of dataframe over all datapoints

    Args:
        df (pandas dataframe): dataframe containing time and value data
        valueColumn (string): name of value data column

    Returns:
        pandas Dataframe: mean hourly value
    """

    # df['Hour'] = df['Timestamp'].dt.hour # this is super bad... the functions change the dataframe directly and only return a none type wtf... help

    return df.groupby(['Hour'])[valueColumn].mean()



def reassignTimestamp(df, timeStampHeader):
    """Redefines the specified column into a datatime format timestamp

    Args:
        df (pandas dataframe): dataframe containing a timestamp like entry
        timeStampHeader (string): name of column containing timestamplike

    Returns:
        pandas dataframe: Dataframe with redefined timestamp
    """
    df['TimeStamp'] = pd.to_datetime(df[timeStampHeader])

    df.drop(timeStampHeader, axis=1, inplace=True)
    
# Sunduration
sunDurationDf = pd.read_csv(r"C:\Users\lelem\Projekte\WetterDatenanalyse\WeatherDataAnalysisESS\Data\cdc_download_2023-05-17_14-28\data\data_OBS_DEU_PT1H_SD.csv", index_col=False)
reassignTimestamp(df=sunDurationDf, timeStampHeader='Zeitstempel')

meanSunDurationYear = calcMeanDaily(df=sunDurationDf, valueColumn='Wert')
meanSunDurationDay = calcMeanHourly(df=sunDurationDf, valueColumn='Wert')


plotMeanDaily(meanDailyValue=meanSunDurationYear, datatitle='Mittlere tägliche Sonnenscheindauer', ylabel='Sonnenscheindauer [h]', minYear=sunDurationDf['Year'].min(), maxYear=sunDurationDf['Year'].max(), location='Essen')
plotMeanHourly(meanHourlyValue=meanSunDurationDay, datatitle='Mittlere stündliche Sonnenscheindauer', ylabel='Sonnenscheindauer [h]', yearLimits=[sunDurationDf['Year'].min(), sunDurationDf['Year'].max()], location='Essen')


# Overcast
overcastDf = pd.read_csv(r"C:\Users\lelem\Projekte\WetterDatenanalyse\WeatherDataAnalysisESS\Data\cdc_download_2023-05-17_14-28\data\data_OBS_DEU_PT1H_RR.csv", index_col=False)
reassignTimestamp(df=overcastDf, timeStampHeader='Zeitstempel')

meanOvercastYear = calcMeanDaily(df=overcastDf, valueColumn='Wert')
meanOvercastDay = calcMeanHourly(df=overcastDf, valueColumn='Wert')


plotMeanDaily(meanDailyValue=meanOvercastYear, datatitle='Mittlerer täglicher Bedeckungsgrad', ylabel='Bedeckungsgrad [Quart]', minYear=overcastDf['Year'].min(), maxYear=overcastDf['Year'].max(), location='Essen')
plotMeanHourly(meanHourlyValue=meanOvercastDay, datatitle='Mittlerer stündlicher Bedeckungsgrad', ylabel='Bedeckungsgrad [Quart]', yearLimits=[overcastDf['Year'].min(), overcastDf['Year'].max()], location='Essen')

# Precipitation
precipitationDf = pd.read_csv(r"C:\Users\lelem\Projekte\WetterDatenanalyse\WeatherDataAnalysisESS\Data\cdc_download_2023-05-17_14-28\data\data_OBS_DEU_PT1H_N.csv", index_col=False)
reassignTimestamp(df=precipitationDf, timeStampHeader='Zeitstempel')

meanPrecipitationYear = calcMeanDaily(df=precipitationDf, valueColumn='Wert')
meanPrecipitationDay = calcMeanHourly(df=precipitationDf, valueColumn='Wert')


plotMeanDaily(meanDailyValue=meanPrecipitationYear, datatitle='Mittlerer täglicher Niederschlag', ylabel='Niederschlag [mm]', minYear=precipitationDf['Year'].min(), maxYear=precipitationDf['Year'].max(), location='Essen')
plotMeanHourly(meanHourlyValue=meanPrecipitationDay, datatitle='Mittlerer stündlicher Niederschlag', ylabel='Niederschlag [mm]', yearLimits=[precipitationDf['Year'].min(), precipitationDf['Year'].max()], location='Essen')
plt.show()
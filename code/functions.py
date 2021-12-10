import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_DIRECTORY = '../data/'
FIGURE_DIRECTORY = '../fig/'
FIGURE_DPI = 600

# List of survey response codes corresponding to answers which provide no info
UNKNOWN_VALUES = [77.0, 99.0]

def create_df_csv(path):
    '''
    @param path: str, path of CSV file to read
    @returns DataFrame created from CSV file
    '''

    return pd.read_csv(DATA_DIRECTORY+path)

def create_df_sas(link, cols):
    '''
    @param link: string for link to read data from XPORT or SAS7BDAT files
    @param cols: list of strings representing names for columns
    @returns DataFrame created from sas file
    '''

    df = pd.read_sas(link)
    df.columns = cols

    return df

def merge_dfs(df1, df2, col):
    '''
    @param df1, df2: DataFrames to merge
    @param on: string of column to merge on
    @returns DataFrame resulting from merging df1 and df2 on col
    '''

    return pd.merge(df1, df2, on=col)

def generate_csv(df, path, header, index, sep, mode):
    '''
    @param df: pd.DataFrame, the DataFrame to create a csv from
    @param path: str, the file path of the csv to generate
    @param header: Boolean, write column names
    @param index: Boolean, write row names
    @param sep: str, the separator character between each entry
    @param mode: str, Python write mode

    Creates a csv at path with the data in df
    '''

    df.to_csv(DATA_DIRECTORY+path, header=header, index=index, sep=sep, mode=mode)

def save_figure(path):
    '''
    @param path: string of path for the created figure
    '''

    plt.savefig(FIGURE_DIRECTORY+path, dpi=FIGURE_DPI)

def remove_unknowns(df):
    '''
    @param df: DataFrame to remove unknown values from
    @returns df with UNKNOWN_VALUES replaced with NaN
    '''

    return df.replace(UNKNOWN_VALUES, np.nan)

def impute(df, dict):
    '''
    @param df: DataFrame to perform imputation on
    @param dict: dictionary of key=column and val=imputation value(s)
    @returns df with imputation performed on all columns within dict
    '''
    
    return df.fillna(value=dict)
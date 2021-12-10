import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FIGURE_DIRECTORY = '../fig/'
FIGURE_DPI = 600

def create_df_sas(link, cols):
    '''
    @param link: string for link to read data from XPORT or SAS7BDAT files
    @param cols: list of strings representing names for columns
    '''
    df = pd.read_sas(link)
    df.columns = cols

    return df

def merge_dfs(df1, df2, col):
    '''
    @param df1, df2: DataFrames to merge
    @param on: string of column to merge on
    '''

    return pd.merge(df1, df2, on=col)

def save_figure(path):
    '''
    @param path: string of path for the created figure
    '''
    plt.savefig(FIGURE_DIRECTORY+path, dpi=FIGURE_DPI)
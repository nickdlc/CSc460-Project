import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, precision_score, recall_score

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

def run_decision_tree(df, features, labels, test_size, random_state):
    '''
    @param df: DataFrame which decision tree is run on
    @param test_size: proportion of data to be used for testing
    @param random_state: random seed for random function
    '''
    
    # Separate features and labels into separate variables
    X,y = df[features], df[labels]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    scaler = MinMaxScaler(feature_range=(0,1))
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    clf = DecisionTreeClassifier(random_state=random_state)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy of Decision Tree: ", accuracy_score(y_test, y_pred))
    print("Precision of Decision Tree: ", precision_score(y_test, y_pred, average='micro'))
    print("Recall of Decision Tree: ", recall_score(y_test, y_pred, average='micro'))
    print("F1 Score of Decision Tree: ", f1_score(y_test, y_pred, average='micro'))

    # Generate confusion matrix
    matrix = confusion_matrix(y_test, y_pred)
    fig = plt.figure(figsize=(8,6))
    ax = sns.heatmap(matrix, annot=True,cmap='Greens', fmt='g')
    plt.title("Confusion Matrix")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    ax.xaxis.set_ticklabels([1.0, 2.0, 3.0, 4.0, 5.0]); 
    ax.yaxis.set_ticklabels([1.0, 2.0, 3.0, 4.0, 5.0]);
    plt.savefig(FIGURE_DIRECTORY+'confusion_matrix.png', dpi=FIGURE_DPI)
    print('Successfully created '+FIGURE_DIRECTORY+'confusion_matrix.png')

    # Generate normalized confusion matrix
    normalized = matrix/matrix.astype(np.float).sum(axis=1)
    fig = plt.figure(figsize=(8,6))
    ax = sns.heatmap(normalized, annot=True,cmap='Greens', fmt='g')
    plt.title("Normalized Confusion Matrix")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    ax.xaxis.set_ticklabels([1.0, 2.0, 3.0, 4.0, 5.0]); 
    ax.yaxis.set_ticklabels([1.0, 2.0, 3.0, 4.0, 5.0]);
    plt.savefig(FIGURE_DIRECTORY+'normalized_confusion_matrix.png', dpi=FIGURE_DPI)
    print('Successfully created '+FIGURE_DIRECTORY+'normalized_confusion_matrix.png')

    # Define the grid of values for tol and max_iter
    tol = [0.01, 0.001, 0.0001]
    max_iter = [1,2,3,4,5]

    # Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
    param_grid = dict(max_depth=max_iter, max_features=['auto', 'sqrt', 'log2', 0.5], min_samples_split=[3,4,5,6])

    # Instantiate GridSearchCV with the required parameters
    grid_model = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5)

    # Fit data to grid_model
    grid_model_result = grid_model.fit(X, y)

    # Summarize results
    best_score, best_params = grid_model_result.best_score_, grid_model_result.best_params_
    print("Best accuracy: %f using %s" % (best_score, best_params))
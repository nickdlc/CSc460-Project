import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions as f

TEST_SIZE = 0.33
RANDOM_STATE = 42

# Create DataFrame from uncleaned data
df = f.create_df_csv('cleaned_data.csv')
# print(df.head(5))

features = [
    'HH ref person\'s gender',
    'HH ref person\'s age in years',
    'HH ref person\'s education level',
    'Race/Hispanic origin w/ NH Asian',
    'Total savings/cash assets for the family',
    #'Annual family income' # delete cuz it bad??
]
labels = [
    'General health condition',
]
f.run_decision_tree(df, features, labels, TEST_SIZE, RANDOM_STATE)
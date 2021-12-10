import pandas as pd
import numpy as np
import statistics
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

### Initial DataFrame Creation
# Create DataFrame for Demographic data
# Refer to # https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm for the data dict
demo_link = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'
demo_cols = ['ID',
             'Data release cycle',
             'Interview/Examination status',
             'Gender',
             'Age in years at screening',
             'Age in months at screening - 0 to 24 mos',
             'Race/Hispanic origin',
             'Race/Hispanic origin w/ NH Asian',
             'Six month time period',
             'Age in months at exam - 0 to 19 years',
             'Served active duty in US Armed Forces',
             'Served in a foreign country',
             'Country of birth',
             'Citizenship status',
             'Length of time in US',
             'Education level - Children/Youth 6-19',
             'Education level - Adults 20+',
             'Marital status',
             'Pregnancy status at exam',
             'Language of SP Interview',
             'Proxy used in SP Interview?',
             'Interpreter used in SP Interview?',
             'Language of Family Interview',
             'Proxy used in Family Interview?',
             'Interpreter used in Family Interview?',
             'Language of MEC Interview',
             'Proxy used in MEC Interview?',
             'Interpreter used in MEC Interview?',
             'Language of ACASI Interview',
             'Total number of people in the Household',
             'Total number of people in the Family',
             '# of children 5 years or younger in HH',
             '# of children 6-17 years old in HH',
             '# of adults 60 years or older in HH',
             'HH ref person\'s gender',
             'HH ref person\'s age in years',
             'HH ref person\'s education level',
             'HH ref person\'s marital status',
             'HH ref person\'s spouse\'s education level',
             'Full sample 2 year interview weight',
             'Full sample 2 year MEC exam weight',
             'Masked variance pseudo-PSU',
             'Masked variance pseudo-stratum',
             'Annual household income',
             'Annual family income',
             'Ratio of family income to poverty']
demo_df = create_df_sas(demo_link, demo_cols)
# print(demo_df.head(5))

# Create DataFrame for Occupation and Income
# Refer to https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OCQ_J.htm for Occupation data dict
# Refer to https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/INQ_J.htm for Income data dict
occ_link = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OCQ_J.XPT'
inc_link = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/INQ_J.XPT'
occ_cols = ['ID',
            'Type of Work', 
            'Hours Worked Last Week', 
            'Usually Work 35 or More Hours?', 
            'Type of Employee', 
            'Months Worked', 
            'Overall Work Schedule', 
            'Main Reason for Not Working', 
            'Kind of Occupation Done the Longest', 
            'Duration of Longest Job']
inc_cols = ['ID',
            'Income from wages/salaries?',
            'Income from self employment?',
            'Income from Social Security or RR?',
            'Income from other disability pension?',
            'Income from retirement/survivor pension?',
            'Income from Supplemental Security Income?',
            'Income from state/county cash assistance?',
            'Income from interest/dividends or rental?',
            'Income from other sources?',
            'Monthly family income',
            'Family monthly poverty level index',
            'Family monthly poverty level category',
            'Family has savings more than $20,000?',
            'Total savings/cash assets for the family',
            'How do you get to the grocery store?']
occ_df = create_df_sas(occ_link, occ_cols)
inc_df = create_df_sas(inc_link, inc_cols)
inc_occ_df = merge_dfs(inc_df, occ_df, 'ID')
# print(inc_occ_df.head(5))

# Merge the Demographic, Income, and Occupation DataFrames for potential features
X_df = merge_dfs(demo_df, inc_occ_df, 'ID')
# print(X_df.head(5))
print('Successfully created potential features DataFrame')

# Create DataFrame for Health Status
# Refer to https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HSQ_J.htm for data dict
healthstat_link = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HSQ_J.XPT'
healthstat_cols = ['ID',
                   'General health condition',
                   'SP have head cold or chest cold',
                   'SP have stomach or intestinal illness?',
                   'SP have flu, pneumonia, ear infection?',
                   'SP donated blood in past 12 months?',
                   'How long ago was last blood donation?',
                   'Blood ever tested for HIV virus?',
                   'Source of Health Status Data']
healthstat_df = create_df_sas(healthstat_link, healthstat_cols)
# print(healthstat_df.head(5))

# Create DataFrame for body measures
# Refer to https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm for data dict
body_link = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.XPT'
body_cols = ['ID',
             'Body Measures Component Status Code',
             'Weight (kg)',
             'Weight Comment',
             'Recumbent Length (cm)',
             'Recumbent Length Comment',
             'Head Circumference (cm)',
             'Head Circumference Comment',
             'Standing Height (cm)',
             'Standing Height Comment',
             'Body Mass Index (kg/m**2)',
             'Upper Leg Length (cm)',
             'Upper Leg Length Comment',
             'Upper Arm Length (cm)',
             'Upper Arm Length Comment',
             'Arm Circumference (cm)',
             'Arm Circumference Comment',
             'Waist Circumference (cm)',
             'Waist Circumference Comment',
             'Hip Circumference (cm)',
             'Hip Circumference Comment']
body_df = create_df_sas(body_link, body_cols)
# print(body_df.head(5))

# Merge the health status and body measure DataFrames for potential labels
y_df = merge_dfs(healthstat_df, body_df, 'ID')
# print(y_df.head(5))

# Create a DataFrame for our desired labels
labels_df = y_df[['ID','General health condition', 'Body Mass Index (kg/m**2)']]
# Select only valid data for self-reported General Health Condition
labels_df = labels_df[labels_df['General health condition'].isin([1.0, 2.0, 3.0, 4.0, 5.0])]
# print(labels_df.head(5))
print('Successfully created labels DataFrame')

# Create a DataFrame for our desired features
features = ['ID',
            'HH ref person\'s gender',
            'HH ref person\'s age in years',
            'HH ref person\'s education level',
            'Race/Hispanic origin w/ NH Asian',
            'Total savings/cash assets for the family',
            'Annual family income']
features_df = X_df[features]
# print(features_df.head(5))

# Combine our features and labels into a single DataFrame
df = merge_dfs(features_df, labels_df, 'ID')
print(df.head(5))
print('Successfully merged features and labels into one DataFrame')

### Exploratory Data Analysis on Initial DataFrames
## Relationship between BMI and General Health Condition
new_ydf = y_df[['Body Mass Index (kg/m**2)','General health condition']]
# Clean dataset by using only rows where GHC=[1,5] and BMI not null
new_ydf = new_ydf[new_ydf['General health condition'].isin([1.0, 2.0, 3.0, 4.0, 5.0])]
new_ydf = new_ydf.dropna(subset=['Body Mass Index (kg/m**2)'])

# Replace BMI in each subgroup with their median
new_ydf['Body Mass Index (kg/m**2)'][new_ydf['Body Mass Index (kg/m**2)'] <= 18.5] = statistics.median(new_ydf['Body Mass Index (kg/m**2)'][new_ydf['Body Mass Index (kg/m**2)'] <= 18.5])
new_ydf['Body Mass Index (kg/m**2)'][(new_ydf['Body Mass Index (kg/m**2)']>18.5) & (new_ydf['Body Mass Index (kg/m**2)']<=25)] = statistics.median(new_ydf['Body Mass Index (kg/m**2)'][(new_ydf['Body Mass Index (kg/m**2)']>18.5) & (new_ydf['Body Mass Index (kg/m**2)']<=25)])
new_ydf['Body Mass Index (kg/m**2)'][(new_ydf['Body Mass Index (kg/m**2)']>25) & (new_ydf['Body Mass Index (kg/m**2)']<=30)] = statistics.median(new_ydf['Body Mass Index (kg/m**2)'][(new_ydf['Body Mass Index (kg/m**2)']>25) & (new_ydf['Body Mass Index (kg/m**2)']<=30)])
new_ydf['Body Mass Index (kg/m**2)'][new_ydf['Body Mass Index (kg/m**2)']>30] = statistics.median(new_ydf['Body Mass Index (kg/m**2)'][new_ydf['Body Mass Index (kg/m**2)']>30])
# Get the count of people in each BMI subgroup and adds it as a column. Then, remove duplicates
new_ydf=new_ydf.value_counts().to_frame().reset_index()
new_ydf=new_ydf.drop_duplicates()


new_bmi = new_ydf['Body Mass Index (kg/m**2)']
new_ghc = new_ydf['General health condition']
plt.scatter(new_bmi, new_ghc, alpha=0.5, s=new_ydf[0])
plt.axvline(x=18.5, color = 'red')
plt.axvline(x=25, color = 'red')
plt.axvline(x=30, color = 'red')
plt.xlabel("BMI")
plt.ylabel("Perceived Health (1 Best-5 Worst)")
plt.title("BMI vs Perceived Health")
save_figure('bmi_ghc.png')
print('Successfully created ../fig/bmi_ghc.png')
# plt.show()

a = np.hstack(y_df['Body Mass Index (kg/m**2)'])
_ = plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.axvline(x=18.5, color = 'red')
plt.axvline(x=25, color = 'red')
plt.axvline(x=30, color = 'red')
plt.title("BMI Histogram")
plt.xlabel("bmi")
plt.ylabel("count")
save_figure('bmi_histogram.png')
print('Successfully created ../fig/bmi_histogram.png')
# plt.show()

a = np.hstack(y_df['General health condition'])
_ = plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.title("Perceived Health Histogram")
plt.xlabel("general health condition")
plt.ylabel("count")
save_figure('ghc_histogram.png')
print('Successfully created ../fig/ghc_histogram.png')
# plt.show()
import pandas as pd
import numpy as np
import functions as f

# Create DataFrame from uncleaned data
df = f.create_df_csv('uncleaned_data.csv')
# print(df.head(5))

### Clean feature columns

## Replace unknown values with NaN and remove difficult data
df['Total savings/cash assets for the family'] = f.remove_unknowns(df['Total savings/cash assets for the family'])

# Remove respondents with 12.0 for "Annual family income" since it is difficult to use this range of annual income
df = df[df['Annual family income'] != 12.0]
df['Annual family income'] = f.remove_unknowns(df['Annual family income'])

# Replace any ranges below $20k with the general "Under $20k" label
df['Annual family income'] = df['Annual family income'].replace([1.0, 2.0, 3.0, 4.0], 13.0)

# Re-index the feature values
ann_fam_income_map = dict(enumerate([13.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 14.0, 15.0]))

# Replace the current feature values with the enumerated ones
df['Annual family income'] = df['Annual family income'].replace(ann_fam_income_map.values(), ann_fam_income_map.keys())

## HH ref person's education level, Total savings/cash asssets for the family, and Annual family income
# value_counts().index[0] => mode imputation
imputation_dict = {
    "HH ref person's education level": df["HH ref person's education level"].value_counts().index[0],
    "Total savings/cash assets for the family": df["Total savings/cash assets for the family"].value_counts().index[0],
    "Annual family income": df["Annual family income"].median()
}
df = f.impute(df, imputation_dict)
# print(df.isna().sum())

### Clean label columns
## Remove NA BMI values since there is only a small number of them and imputing makes little sense
df = df[df['Body Mass Index (kg/m**2)'].notna()]
print(df.isna().sum())

### Export cleaned data csv
f.generate_csv(df, 'cleaned_data.csv', True, False, ',', 'w')
print('Successfully created ../data/cleaned_data.csv')
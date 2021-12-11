# Forecasting Your General Well-Being

### Group Members
- Nicholas De La Cruz
- Kareem Ibrahim
- Gene Lam

### Repository Structure
- `data`
  - `uncleaned_data.csv`: The uncleaned data from our exploratory analysis
  - `cleaned_data.csv`: The data after cleaning
  - `data_dict.csv`: The data dictionary for our cleaned data
- `code`
  - `eda.py`: Contains all of the code for our exploratory analysis
  - `data_cleaning.py`: Cleans our data and exports it as a CSV in `../data/cleaned_data.csv`
  - `build_dtree.py`: Builds the decision tree based on the data from `../data/cleaned_data.csv`
  - `functions.py`: Contains functions used throughout the entire project
- `fig`
  - `bmi_ghc.png`: BMI vs GHC scatterplot
  - `bmi_histogram.png`: BMI histogram
  - `confusion_matrix.png`: Confusion matrix of classification
  - `ghc_histogram.png`: GHC histogram
  - `normalized_confusion_matrix.png`: Normalized confusion matrix of classification
  - `pca_cumvariance.png`: PCA cumulative variance graph
  - `pca_variance.png`: PCA variance graph
  - `roc_curve.png`: ROC curve 
- `Full_Analysis.ipynb`: Notebook containing our EDA, Data Cleaning, and Initial Models. All updates since the initial preliminary analysis are also included in here.
- `README.md`: README file
- `blog_post.md`: Blog post with Motivation, Data, Evaluation, and Future Work
- `final_analysis.md`: Final analysis with Repository Structure, Challenges, Contributions
- `preliminary_analysis.md`: Preliminary analysis with Data Cleaning Code, Exploratory Analysis, Challenges, Future Work, and Contributions

### Challenges (Optional)
We encountered a few challenges for this assignment. One challenge we had was mapping the column codes from the NHANES survey to the columns within the spreadsheets. The columns in the initial dataset are coded, and it required us to change the values of the column labels to those found on the NHANES website.
Another challenge we encountered was for cleaning the data. For the features we decided on, there were some inputs that didn't show up as NaN, such as "Refused" or "Don't Know" values, that we needed to account for. In most cases, we decided to impute NaN values with either the mode or median of the set. The primary issue, however, was cleaning the family income field. We wanted to impute NaN values with the median of this column, but the values from the data dictionary were not linear. For example, the code 13 represented an income of "Under $20,000" while the code of 14 represented "$75,000 - $99,000". We decided to combine the codes of 1-4, which represented $0 to $20,000, with the under $20,000 code, deleted the code 12 of over $20,000, and set all missing or don't know values to NaN. We then relabeled all of the codes from 0 to 15 in order of higher income. This allowed us to calculate the median and impute all NaN's with this value.

### Contributions
- Nicholas De La Cruz: Data cleaning, classification, linear regression
- Kareem Ibrahim: Data cleaning, improving the model
- Gene Lam: Exploratory data analysis, confusion matrix, ROC, and PCA

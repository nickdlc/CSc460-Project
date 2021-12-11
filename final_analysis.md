# Forecasting Your General Well-Being (Final Analysis)

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
In our preliminary analysis, the challenges we faced were mapping the column names from their keys to their definitions, and cleaning the data because we were working with a large dataset. After we chose a manageable amount of feature vectors to work with, this was no longer a problem. Our biggest problem during the Final Analysis was improving our machine learning model. We performed a classification using decision tree and linear regression. However, the initial accuracy for both was around 41% and 6% respectively. We tried a bunch of techniques to improve our models.

### Contributions
- Nicholas De La Cruz: Data cleaning, classification, KFold, cross-validation, linear regression, translating main notebook into scripts
- Kareem Ibrahim: Data cleaning, improving the model, KFold, cross-validation
- Gene Lam: Exploratory data analysis, confusion matrix, ROC, and PCA

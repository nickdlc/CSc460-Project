# Project Title

### Group Members
- Nicholas De La Cruz
- Kareem Ibrahim
- Gene Lam

### Repository Structure

For example:
- `data`
  - `cleaned_data.csv`: The cleaned data from our preliminary analysis
  - `data_dict.csv`: The data dictionary for our cleaned data
- `code`
  - `Premliminary_Analysis.ipynb`: Contains our EDA, data cleaning, and initial models
  - `eda.py`: Contains all of the code for our exploratory analysis
  - `data_cleaning.py`: Cleans our data and exports it as a CSV in `./data/cleaned_data.csv`
  - `build_dtree.py`: Builds the decision tree based on the data from `cleaned_data.csv`

### Exploratory Analysis
In our exploratory data analysis, we figured out what features we would like to use to predict the health outcomes of people who took the National Health and Nutrition Examination Survey (NHANES). This is a government funded annual survey to gauge the public's current health status. Within the survey results, there are numerous spreadsheets of reported health information. We merged a few of these spreadsheets together in order to find the features and labels necessary to solve our problem. The features we decided on are 
1. HH ref person's gender
1. HH ref person's age in years                   
1. HH ref person's education level              
1. Race/Hispanic origin w/ NH Asian               
1. Total savings/cash assets for the family    
1. Annual family income                         
1. General health condition                       
1. Body Mass Index (kg/m**2)                     
in order to predict a person's BMI and General Health Condition (GHC). We believe that by using a person's identifiable attributes alongside their household economic status, we can gauge their general health condition. We chose the labels of BMI and GHC because we believe that they can accurately classify a person's healthiness. Note, BMI might be an unreliable label on its own, and GHC is a self-reported value which may also be untrustworthy. However, using both of these as our predicted labels may prove to yield a more accurate analysis of a person's well-being.

### Challenges
We encountered a few challenges for this assignment. One challenge we had was mapping the column codes from the NHANES survey to the columns within the spreadsheets. The columns in the initial dataset are coded and it required us to change the values of the column labels to those found on the NHANES website.
Another challenge we encountered was for cleaning the data. For the features we decided on, there were some inputs that didn't show up as NaN, such as "Refused" or "Don't Know" values, that we needed to account for. In most cases, we decided to impute NaN values with either the mode or median of the set. The primary issue, however, was cleaning the family income field. We wanted to impute NaN values witht he median of this column, but the values from the data dictionary were not linear. For example, the code 13 represented an income of "Under $20,000" while the code of 14 represented "$75,000 - $99,000". We decided to combine the codes of 1-4, which represented $0 to $20,000, with the under $20,000 code, deleted the code 12 of over $20,000, and set all missing or don't know values to NaN. We then relabeled all of the codes from 0 to 15 in order of higher income. This allowed us to calculate the median and impute all NaN's with this value.

### Future Work


### Contributions
Describe the contributions that each group member made.
